import lib.db as db
from lib.generic import typehint
from pygments import highlight
from pygments.lexers import (get_lexer_for_filename,)
from pygments.formatters import HtmlFormatter
import json
from lib.config import Config

class PasteNotFound(Exception):
        pass

class Paste:

        def __init__(self, args):
                self.code_id = args[0]
                self.date = args[1]
                self.code = args[2]
                self.private = args[4]
                self.key = args[3]

        def drop(self):
                db.Code().delete(self.code_id)

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
            for row in db.Code().all(private):
                    a.append(Paste(list(row)))
            return a
        
        @classmethod
        def all_json(self,private=False):
            a = list()
            for entry in Paste.all(private):
                a.append(entry.json(False))
            return json.dumps(a, sort_keys=True, indent=4)


        @classmethod
        def new(self, code, private):
            a = Config()
            a.parse()
            keylen = [a.paste_pub_len,a.paste_priv_len][private]
            return db.Code().add(code, private, int(keylen))

        @classmethod
        @typehint
        def find(self,key: str):
            code = db.Code().find(key)
            return Paste(code)

