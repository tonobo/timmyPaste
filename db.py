import sqlite3
import datetime
import random
import string

class Database:

	def __init__(self,name=None):
		if name:
			self.__db = sqlite3.connect(name)
		else:
			self.__db = sqlite3.connect('app.sqlite3')
		if not self.__table_exists():
			self.__initial_setup()

	def add(self,code,keylen,date=datetime.datetime.now()):
		cursor = self.__db.cursor()
		key = "".join([random.choice(string.ascii_letters[:26]) for i in range(keylen)])
		cursor.execute('''
			INSERT INTO code(code,date,key) VALUES (?,?,?)''',
			(code, date,key,))
		self.__db.commit()
		return key

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
			''', (id,))
		return cursor.fetchone()
	
	def all(self):
		cursor = self.__db.cursor()
		cursor.execute('''
			SELECT * 
				FROM code
			''')
		return cursor.fetchall()

	def __initial_setup(self):
		cursor = self.__db.cursor()
		cursor.execute('''
			CREATE TABLE code (
				id 		INTEGER PRIMARY KEY AUTOINCREMENT,
				date 	TEXT NOT NULL,
				code	TEXT NOT NULL,
				key 	TEXT NOT NULL 
			)''')
		self.__db.commit()

	def __table_exists(self):
		cursor = self.__db.cursor()
		cursor.execute('''
			SELECT name 
				FROM sqlite_master 
				WHERE type="table" AND 
							name="code" ''')
		return bool(cursor.fetchone())
