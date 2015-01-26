from lib.db.database import *
from datetime import datetime
import random
import string
    
class KeyNotFound(Exception):
    pass

class Url(Database.Methods):

    @typehint
    def add(self,
            url: str,
            keylen: int,
            date: datetime = datetime.now()) -> None:

            cursor = self.conn().cursor()
            for i in range(0, 100):
                key = "".join([random.choice(string.ascii_letters) for i in range(keylen)])
                try:
                    cursor.execute('''
                        INSERT INTO url(url,date,key) VALUES (?,?,?)''',
                        (url,date,key))
                    self.conn().commit()
                    return key
                except:
                    continue
            raise Exception("Increase key length")

    def drop(self):
        super().drop()

    def create(self):
        super().create('''
            CREATE TABLE url (
              id      INTEGER PRIMARY KEY AUTOINCREMENT,
              date    TEXT NOT NULL,
              url     TEXT NOT NULL,
              key     TEXT NOT NULL UNIQUE
            )''')

    @typehint
    def delete(self,key: str) -> None:
            cursor = self.conn()
            cursor.execute('DELETE FROM url WHERE key = ?', (key,))
            self.conn().commit()

    @typehint
    def find(self,key: str) -> tuple:
            cursor = self.conn().cursor()
            cursor.execute('SELECT * FROM url WHERE key = ?', (key,))
            a = cursor.fetchone()
            if a:
                return a
            raise KeyNotFound('Key invalid.')

    @typehint
    def all(self) -> list:
            cursor = self.conn().cursor()
            cursor.execute('SELECT * FROM url')
            return [i[:-1]+(bool(i[-1]),) for i in cursor.fetchall()]

Database.Methods.register(Url)
