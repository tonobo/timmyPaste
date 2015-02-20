from lib.db.database import *
import lib.db.key
from datetime import datetime
import random
import string
    
class Url(Database.Methods):

    @typehint
    def add(self,
            url: str,
            keylen: int,
            date: datetime = datetime.now()) -> None:

            key_id = lib.db.key.Key().add("Url",keylen)
            self.sql('INSERT INTO url(url,key_id) VALUES (?,?)',
                        (url,key_id[0]))
            return key_id[3]

    def drop(self):
        super().drop()

    def create(self):
        super().create('''
            CREATE TABLE url (
              id      INTEGER PRIMARY KEY AUTOINCREMENT,
              key_id  INTEGER NOT NULL REFERENCES key(id) ON DELETE CASCADE,
              url     TEXT NOT NULL
            )''')

    @typehint
    def find(self,key: str) -> tuple:
            cursor = self.conn().cursor()
            cursor.execute('''
                SELECT url.id,date,url,key
                FROM url
                INNER JOIN key ON key = ?''', (key,))
            return cursor.fetchone()

    @typehint
    def all(self) -> list:
            cursor = self.conn().cursor()
            cursor.execute('''
                SELECT url.id,date,url,key
                FROM url
                INNER JOIN key ON key_id = key.id''')
            return cursor.fetchall()

Database.Methods.register(Url)
