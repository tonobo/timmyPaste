import configparser

class Config:

    def __init__(self):
        self.c = configparser.ConfigParser()
            
    def parse(self):
        self.c.read_file(open('app.cfg'))
        self.paste_priv_len = self.c['Paste']['key_length_private']
        self.paste_pub_len =  self.c['Paste']['key_length_public']
        self.url_len =        self.c['Url']['key_length']
        self.app_locale =     self.c['App']['locale']
        self.db_name =        self.c['App']['db_name']
        self.url =            self.c['App']['url']
            

