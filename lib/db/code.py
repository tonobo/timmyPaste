from lib.db.database import *
from datetime import datetime
import random
import string

class Code(Database.Methods):

    class KeyNotFound(Exception):
        pass

    class KeyToShortError(Exception):
        pass

    @typehint
    def add(self,
            code: str,
            is_private: bool,
            keylen: int,
            date: datetime = datetime.now()) -> None:

            cursor = self.conn().cursor()
            for i in range(0, 100):
                key = "".join([random.choice(string.ascii_letters) for i in range(keylen)])
                try:
                    cursor.execute('''
                        INSERT INTO code(code,date,key,private) VALUES (?,?,?,?)''',
                        (code,date,key,int(is_private)))
                    self.conn().commit()
                    return key
                except:
                    continue
            raise KeyToShortError("Increase key length")

    def drop(self):
        super().drop()

    def create(self):
        super().create('''
            CREATE TABLE code (
              id      INTEGER PRIMARY KEY AUTOINCREMENT,
              date    TEXT NOT NULL,
              code    TEXT NOT NULL,
              key     TEXT NOT NULL UNIQUE,
              private INTEGER NOT NULL
            )''')

    @typehint
    def delete(self,key: str) -> None:
            cursor = self.conn()
            cursor.execute('DELETE FROM code WHERE key = ?', (key,))
            self.conn().commit()

    @typehint
    def find(self,key: str) -> tuple:
            cursor = self.conn().cursor()
            cursor.execute('SELECT * FROM code WHERE key = ?', (key,))
            a = cursor.fetchone()
            if a:
                return a[:-1]+(bool(a[-1]),)
            raise KeyNotFound('Invalid key was given.')

    @typehint
    def all(self, private: bool) -> list:
            cursor = self.conn().cursor()
            cursor.execute('''SELECT * FROM code WHERE private = ?''', 
                    (private,))
            return [i[:-1]+(bool(i[-1]),) for i in cursor.fetchall()]

Database.Methods.register(Code)
