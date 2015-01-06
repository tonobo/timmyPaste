from lib.db import Database
from pygments import highlight
from pygments.lexers import (get_lexer_for_filename,)
from pygments.formatters import HtmlFormatter
import json
from lib.config import Config

class CodeNotFound(Exception):
        pass

class Code:

        def __init__(self, args):
                self.code_id = args[0]
                self.date = args[1]
                self.code = args[2]
                self.private = args[4]
                self.key = args[3]

        def drop(self):
                Database().delete(self.code_id)

        def highlight(self,filename):
                lex = get_lexer_for_filename(filename)
                return highlight(self.code, lex, HtmlFormatter())
       
        def json(self, dump=True):
            h={
                'date': self.date,
                'code': self.code,
                'key': self.key,
                'is_private': self.private
            }
            if dump:
                return json.dumps(h, sort_keys=True, indent=4)
            return h

        @classmethod
        def all(self, private=False):
            a = list()
            for row in Database().all(private):
                    a.append(Code(list(row)))
            return a
        
        @classmethod
        def all_json(self,private=False):
            a = list()
            for entry in Code.all(private):
                a.append(entry.json(False))
            return json.dumps(a, sort_keys=True, indent=4)


        @classmethod
        def new(self, code, private):
            a = Config()
            a.parse()
            keylen = [a.pub_key_len,a.priv_key_len][private]
            db = Database()
            return db.add(code, private, int(keylen))

        @classmethod
        def find(self,key: str) -> str:
            db = Database()
            code = db.find(key)
            if code:
                return Code(code)
            raise CodeNotFound('Code element not found.')

