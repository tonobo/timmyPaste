import sqlite3
import datetime
import random
import string

class Database:

        def __init__(self,name='app.sqlite'):
                self.__db = sqlite3.connect(name)

        def add(self,code,is_private,keylen,date=datetime.datetime.now()):
                cursor = self.__db.cursor()
                key = "".join([random.choice(string.ascii_letters[:26]) for i in range(keylen)])
                for i in range(0, 100):
                    try:
                        cursor.execute('''
                            INSERT INTO code(code,date,key,private) VALUES (?,?,?,?)''',
                            (code, date,key,int(is_private)))
                        self.__db.commit()
                        return key
                    except:
                        continue

        def delete(self,id):
                cursor = self.__db.cursor()
                cursor.execute('''
                        DELETE FROM code WHERE id = ?''', (id,))
                self.__db.commit()
 
        def find(self,key):
                cursor = self.__db.cursor()
                cursor.execute('''
                        SELECT * 
                                FROM code
                                WHERE key = ?
                        ''', (key,))
                a = cursor.fetchone()
                if a:
                    return a[:-1]+(bool(a[-1]),)
        
        def all(self, private):
                cursor = self.__db.cursor()
                cursor.execute('''
                        SELECT * 
                                FROM code
                                WHERE private = ?
                        ''', (private,) )
                return [i[:-1]+(bool(i[-1]),) for i in cursor.fetchall()]
        
        def drop(self):
            if self.table_exists():
                cursor = self.__db.cursor()
                cursor.execute('DROP TABLE code')

        def create(self):
            if not self.table_exists():
                cursor = self.__db.cursor()
                cursor.execute('''
                        CREATE TABLE code (
                                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                                date    TEXT NOT NULL,
                                code    TEXT NOT NULL,
                                key     TEXT NOT NULL UNIQUE,
                                private INTEGER NOT NULL
                        )''')
                self.__db.commit()

        def table_exists(self):
                cursor = self.__db.cursor()
                cursor.execute('''
                        SELECT name 
                                FROM sqlite_master 
                                WHERE type="table" AND 
                                name="code" ''')
                return bool(cursor.fetchone())
