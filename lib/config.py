import configparser

class Config:

    def __init__(self):
        self.c = configparser.ConfigParser()
            
    def parse(self):
        self.c.read_file(open('app.cfg'))
        self.priv_key_len = self.c['Keys']['length_private']
        self.pub_key_len =  self.c['Keys']['length_public']
        self.app_locale =   self.c['App']['locale']
            

