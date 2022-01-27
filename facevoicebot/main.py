import os
import telebot

from storage import Storage
from process import detect_face, process_voice


def main():
    bot = telebot.TeleBot(os.getenv('TOKEN'))
    storage = Storage(os.getenv('DATABASE_URL'))
    admin_id = os.getenv('ADMIN_ID')

    def get_file(file_id):
        file_info = bot.get_file(file_id)
        file_to_buf = bot.download_file(file_info.file_path)
        return file_to_buf, file_info

    def send_message(chat_id, text, item=None):
        if item and item[2] == 'photo':
            bot.send_photo(chat_id, photo=item[3], caption=text)
            if admin_id:
                bot.send_photo(admin_id, photo=item[3],
                               caption="[Admin] " + text)
        elif item and item[2] == 'voice':
            bot.send_audio(chat_id, audio=item[3], caption=text,
                           title=f"{item[0]}.wav")
            if admin_id:
                bot.send_audio(admin_id, audio=item[3],
                               caption="[Admin] " + text,
                               title=f"{item[0]}.wav")
        else:
            bot.send_message(chat_id, text)
            if admin_id:
                bot.send_message(admin_id, "[Admin] " + text)
        print(chat_id, text)

    @bot.message_handler(content_types=['photo'])
    def handle_photo(message):
        file_to_buf, file_info = get_file(message.photo[-1].file_id)
        n_faces, p_img = detect_face(file_to_buf)

        if not p_img:
            feedback = ("No faces found. Photo didn't save. You can try "
                        + "to send the photo without comporession.")
            send_message(message.chat.id, feedback)
        else:
            feedback = f'Detected: {n_faces} faces. Photo saved!'
            send_message(message.chat.id, feedback,
                         [None, message.chat.id, 'photo', p_img])
            storage.save_item(message.chat.id, 'photo', file_to_buf)

    @bot.message_handler(content_types=['voice'])
    def handle_voice(message):
        file_to_buf, file_info = get_file(message.voice.file_id)
        bit_rate, wav_voice = process_voice(file_to_buf)

        file_id = storage.save_item(message.chat.id, 'voice', wav_voice)
        feedback = (f'Voice message `{file_info.file_path}` received,'
                    + f' processed and saved: `{file_id}.wav`'
                    + f' ({int(bit_rate/1000)} kbps).')
        send_message(message.chat.id, feedback)

    @bot.message_handler(commands=['photo', 'voice'])
    def handle_command_photo_voice(message):
        command = message.text[1:].split(" ", 2)
        item_type = command[0]
        item_id = int(storage.count_items(message.chat.id, item_type))

        if len(command) == 2:
            if command[1].isdigit() and (0 < int(command[1]) <= item_id):
                item_id = int(command[1])
                item = storage.get_item(message.chat.id, item_type, item_id)
                text = f"{item_type}: {item_id}"
                send_message(message.chat.id, text, item)
            else:
                send_message(message.chat.id, "Wrong request.")

        else:
            if item_id:
                item = storage.get_last_item(message.chat.id, item_type)
                text = (f'You have {item_id} saved {item_type}-files.'
                        + ' This is the last one.')
                send_message(message.chat.id, text, item)
            else:
                send_message(message.chat.id,
                             f"You don't have any {item_type}-files.")

    @bot.message_handler(commands=['reset'])
    def handle_command_reset(message):
        command = message.text[1:].split(" ", 2)

        if len(command) == 1:
            send_message(message.chat.id,
                         "You need to specify your request. "
                         + "Use `/reset photos` or `/reset voices`.")
            return

        if command[1] == 'photos':
            storage.reset(message.chat.id, 'photo')
            send_message(message.chat.id,
                         "All saved photos are deleted.")
        elif command[1] == 'voices':
            storage.reset(message.chat.id, 'voice')
            send_message(message.chat.id,
                         "All saved voice messages are deleted.")
        else:
            send_message(message.chat.id, "Wrong request.")

    @bot.message_handler(commands=['start'])
    def handle_command_start(message):
        text = ("Bot is waiting photo or voice message. "
                + "If the bot detects at least one face in the photo, "
                + "the photo is saved. Voice message will be processed "
                + "at sampling rate 16 kHz (256 kbps) and saved.")
        send_message(message.chat.id, text)

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        send_message(message.chat.id, "Send a photo or a voice message.")

    @bot.message_handler(
            content_types=['document'],
            func=lambda message: message.document.mime_type[:5] == 'image')
    def handle_document(message):
        file_to_buf, file_info = get_file(message.document.file_id)
        n_faces, p_img = detect_face(file_to_buf)

        if not p_img:
            feedback = "No faces found. Photo didn't save."
            send_message(message.chat.id, feedback)
        else:
            feedback = f'Detected: {n_faces} faces. Photo saved!'
            send_message(message.chat.id, feedback,
                         [None, message.chat.id, 'photo', p_img])
            storage.save_item(message.chat.id, 'photo', file_to_buf)

    storage.create_table()
    print("Bot polling...")
    bot.polling()


if __name__ == '__main__':
    main()
