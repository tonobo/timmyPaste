import configparser

class Config:

    def __init__(self):
        self.c = configparser.ConfigParser()
            
    def defaults(self):
        self.c['Keys'] = {
                'length_public': 8,
                'length_private': 50
                }
        self.c.write(open('app.cfg', 'w'))

    def parse(self):
        self.c.read_file(open('app.cfg'))
        self.priv_key_len = self.c['Keys']['length_private']
        self.pub_key_len = self.c['Keys']['length_public']
            

