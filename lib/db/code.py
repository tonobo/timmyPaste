from lib.db.database import *
import lib.db.key
from datetime import datetime
import random
import string

class Code(Database.Methods):

    @typehint
    def add(self,
            code: str,
            is_private: bool,
            keylen: int) -> str:

            key_id = lib.db.key.Key().add("Code",keylen)
            self.sql('INSERT INTO code(code,key_id,private) VALUES (?,?,?)',
                        (code,key_id[0],int(is_private),))
            return key_id[3]

    def drop(self):
        super().drop()

    def create(self):
        super().create('''
            CREATE TABLE code (
              id      INTEGER PRIMARY KEY AUTOINCREMENT,
              key_id  INTEGER NOT NULL REFERENCES key(id) ON DELETE CASCADE,
              code    TEXT NOT NULL,
              private INTEGER NOT NULL
            )''')

    @typehint
    def find(self,key: str) -> tuple:
            cursor = self.conn().cursor()
            cursor.execute('''
                SELECT code.id,key,date,code,private 
                FROM code 
                INNER JOIN key ON key = ?''', 
                (key,))
            a = cursor.fetchone()
            return a[:-1]+(bool(a[-1]),)

    @typehint
    def all(self, private: bool) -> list:
            cursor = self.conn().cursor()
            cursor.execute('''
                SELECT code.id,key,date,code,private 
                FROM code 
                INNER JOIN key ON key_id = key.id
                WHERE private = ?''', 
                    (private,))
            return [i[:-1]+(bool(i[-1]),) for i in cursor.fetchall()]

Database.Methods.register(Code)
