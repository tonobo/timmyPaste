import lib.db as db
from lib.generic import typehint
import json
from lib.config import Config

class Url:

        def __init__(self, args):
                self.url_id = args[0]
                self.date = args[1]
                self.url = args[2]
                self.key = args[3]

        def drop(self):
                db.Url().delete(self.url_id)

        def json(self, dump=True):
            h={
                'date': self.date,
                'url': self.url,
                'key': self.key
            }
            if dump:
                return json.dumps(h, sort_keys=True, indent=4)
            return h

        @classmethod
        def all(self):
            a = list()
            for row in db.Url().all():
                    a.append(Url(list(row)))
            return a
        
        @classmethod
        def all_json(self):
            a = list()
            for entry in Url.all():
                a.append(entry.json(False))
            return json.dumps(a, sort_keys=True, indent=4)


        @classmethod
        def new(self, url):
            a = Config()
            a.parse()
            return db.Url().add(url, int(a.url_len))

        @classmethod
        @typehint
        def find(self,key: str):
            url = db.Url().find(key)
            return Url(url)

