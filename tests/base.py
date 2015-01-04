import unittest
import app
from lib.db import Database
import os

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.db = Database('dev.sqlite3')
        app.app.testing = True
        self.app = app.app.test_client()
        self.db.create()

    def tearDown(self):
        self.db.drop()
        os.remove('dev.sqlite3')

