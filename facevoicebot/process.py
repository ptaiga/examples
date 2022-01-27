import cv2
import numpy as np

from io import BytesIO
from pydub import AudioSegment


def detect_face(buf):
    path_to_face_detector = 'opencv/haarcascade_frontalface_default.xml'
    buf_to_np = np.frombuffer(buf, dtype=np.uint8)
    img_raw = cv2.imdecode(buf_to_np, cv2.IMREAD_COLOR)

    img_gray = cv2.cvtColor(img_raw, cv2.COLOR_BGR2GRAY)
    haar_cascade_face = cv2.CascadeClassifier(path_to_face_detector)
    faces_rects = haar_cascade_face.detectMultiScale(
        img_gray, scaleFactor=1.25, minNeighbors=5)

    prepared_img = None
    if len(faces_rects) > 0:
        for (x, y, w, h) in faces_rects:
            cv2.rectangle(img_raw, (x, y), (x+w, y+h), (0, 255, 0), 2)

        encode_img = cv2.imencode('.jpg', img_raw)
        prepared_img = encode_img[1].tobytes()

    return len(faces_rects), prepared_img


def process_voice(buf):
    frame_rate = 16000
    sample_width = 2
    bit_rate = frame_rate * sample_width * 8
    voice = AudioSegment.from_ogg(BytesIO(buf))
    voice_processed = voice.set_frame_rate(16000).set_sample_width(2)
    return bit_rate, voice_processed.export(format='wav').read()
