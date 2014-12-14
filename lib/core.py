from lib.db import Database
from pygments import highlight
from pygments.lexers import (get_lexer_for_filename,)
from pygments.formatters import HtmlFormatter

class CodeNotFound(Exception):
        pass

class Code:

        def __init__(self, args):
                self.code_id = args[0]
                self.date = args[1]
                self.code = args[2]

        def drop(self):
                Database().delete(self.code_id)

        def highlight(self,filename):
                lex = get_lexer_for_filename(filename)
                return highlight(self.code, lex, HtmlFormatter())
        
        @classmethod
        def all(self, private=False):
                db = Database()
                a = list()
                for row in db.all(private):
                        a.append(Code(list(row)))
                return a

        @classmethod
        def new(self, code, private, keylen=10):
                db = Database()
                return db.add(code, private, keylen)

        @classmethod
        def find(self,key: str) -> str:
                db = Database()
                code = db.find(key)
                if code:
                        return Code(code)
                raise CodeNotFound('Code element not found.')

