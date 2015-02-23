import unittest
import app
from lib.db import *
from lib.db.database import *
import os

class BaseTest(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()

    def tearDown(self):
        pass
