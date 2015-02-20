from lib.db.database import *
from datetime import datetime
import random
import string

class Key(Database.Methods):

    class KeyNotFound(Exception):
        pass

    class KeyToShortError(Exception):
        pass

    @typehint
    def add(self,
            kind: str,
            keylen: int,
            date: datetime = datetime.now()) -> tuple:

            cursor = self.conn().cursor()
            for i in range(0, 100):
                key = "".join([random.choice(
                    string.ascii_letters+"0123456789_-:([]{})!"
                    ) for i in range(keylen)])
                try:
                    cursor.execute('''
                        INSERT INTO key(kind,date,key) VALUES (?,?,?)''',
                        (kind,date,key,))
                    self.conn().commit()
                    return self.find(key)
                except sqlite3.IntegrityError:
                    pass
                except sqlite3.OperationalError:
                    break
            raise KeyToShortError("Increase key length")

    @typehint
    def get_klazz(self,key: str):
        klazz = self.find(key)[2]
        exec("import lib.{0}".format(klazz.lower()))
        return eval("lib.{0}.{1}.find(key)".format(klazz.lower(),klazz))

    def drop(self):
        super().drop()

    def create(self):
        super().create('''
            CREATE TABLE key (
              id      INTEGER PRIMARY KEY AUTOINCREMENT,
              date    TEXT NOT NULL,
              kind    TEXT NOT NULL,
              key     TEXT NOT NULL UNIQUE
            )''')

    @typehint
    def find(self,key: str) -> tuple:
            cursor = self.conn().cursor()
            cursor.execute('SELECT * FROM key WHERE key = ?', (key,))
            a = cursor.fetchone()
            if a:
                return a
            raise KeyNotFound('Invalid key was given.')
    
    @typehint
    def all(self) -> list:
            cursor = self.conn().cursor()
            cursor.execute('SELECT * FROM key')
            return cursor.fetchall()

Database.Methods.register(Key)
