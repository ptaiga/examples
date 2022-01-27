import os
import psycopg2


class Storage:

    def __init__(self, url):
        self.db_url = url

    def open_(self):
        self.conn = psycopg2.connect(self.db_url, sslmode='require')
        self.cur = self.conn.cursor()

    def close(self):
        self.conn.commit()
        self.cur.close()
        self.conn.close()

    def create_table(self):
        if self.db_url:
            self.open_()
            self.cur.execute("CREATE TABLE IF NOT EXISTS test \
                (id serial primary key, user_id integer not null, \
                item_type text, item bytea not null);")
            self.close()
        else:
            self.items = {}
            self.store = '.store'
            if not os.path.exists(self.store):
                os.mkdir(self.store)

    def save_item(self, user_id, item_type, item):
        if self.db_url:
            self.open_()
            self.cur.execute("INSERT INTO test (user_id, item_type, item) \
                VALUES (%s, %s, %s)", (user_id, item_type, item))
            self.cur.execute("SELECT COUNT(*) FROM test \
                WHERE user_id = %s AND item_type = %s;", (user_id, item_type))
            id_ = self.cur.fetchone()[0]
            self.close()

        else:
            ext = {'photo': 'jpg',  'voice': 'wav'}
            if user_id not in self.items:
                self.items[user_id] = {'photo': [], 'voice': []}
            id_ = len(self.items[user_id][item_type]) + 1
            file_name = (f'{self.store}/{user_id}_{item_type}_{id_}'
                         + f'.{ext[item_type]}')
            with open(file_name, 'wb') as f:
                f.write(item)
            self.items[user_id][item_type].append(
                [id_, user_id, item_type, file_name])

        return id_

    def count_items(self, user_id, item_type):
        if self.db_url:
            self.open_()
            self.cur.execute("SELECT COUNT(*) FROM test \
                WHERE user_id = %s AND item_type = %s;", (user_id, item_type))
            last_item_id = self.cur.fetchone()
            self.close()
            return last_item_id[0]

        else:
            if user_id not in self.items:
                self.items[user_id] = {'photo': [], 'voice': []}
            return len(self.items[user_id][item_type])

    def get_all(self, user_id, item_type):
        if self.db_url:
            self.open_()
            self.cur.execute(
                "SELECT * FROM test WHERE user_id = %s AND item_type = %s;",
                (user_id, item_type))
            items = self.cur.fetchall()
            self.close()
        else:
            if user_id not in self.items:
                self.items[user_id] = {'photo': [], 'voice': []}
            items = self.items[user_id][item_type]

        return items

    def get_last_item(self, user_id, item_type):
        if self.db_url:
            self.open_()
            self.cur.execute("SELECT COUNT(*) FROM test \
                WHERE user_id = %s AND item_type = %s;", (user_id, item_type))
            item_id = self.cur.fetchone()[0]
            self.cur.execute(
                "SELECT * FROM test WHERE user_id = %s AND item_type = %s \
                ORDER BY id DESC LIMIT 1;", (user_id, item_type))
            item = list(self.cur.fetchone())
            item[0] = item_id
            self.close()
        else:
            if user_id not in self.items:
                self.items[user_id] = {'photo': [], 'voice': []}
            if len(self.items[user_id][item_type]) > 0:
                item = self.items[user_id][item_type][-1].copy()
                with open(item[3], 'rb') as f:
                    item[3] = f.read()
            else:
                item = None
        return item

    def get_item(self, user_id, item_type, item_id):
        if self.db_url:
            self.open_()
            self.cur.execute(
                "SELECT * FROM test WHERE user_id = %s AND item_type = %s \
                LIMIT %s;", (user_id, item_type, item_id))
            item = list(self.cur.fetchall()[-1])
            item[0] = item_id
            self.close()
        else:
            if user_id not in self.items:
                self.items[user_id] = {'photo': [], 'voice': []}
            if len(self.items[user_id][item_type]) >= item_id:
                item = self.items[user_id][item_type][item_id-1].copy()
                with open(item[3], 'rb') as f:
                    item[3] = f.read()
            else:
                item = None
        return item

    def reset(self, user_id, item_type):
        if self.db_url:
            self.open_()
            self.cur.execute(
                "DELETE FROM test WHERE user_id = %s AND item_type = %s;",
                (user_id, item_type))
            self.close()
        else:
            self.items[user_id][item_type] = []
