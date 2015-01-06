import configparser

class Config:

    def __init__(self):
        self.c = configparser.ConfigParser()
            
    def defaults(self):
        self.c['Keys'] = {
                'length_public': 8,
                'length_private': 50
                }
        self.c['App'] = {
                'title': 'timmyPaste',
                'salutation': 'Hi Dude,',
                'salutation_text': "Try to paste some stuff. :D"
                }
        self.c.write(open('app.cfg', 'w'))

    def parse(self):
        self.c.read_file(open('app.cfg'))
        self.priv_key_len = self.c['Keys']['length_private']
        self.pub_key_len =  self.c['Keys']['length_public']
        self.app_title =    self.c['App']['title']
        self.app_sal =      self.c['App']['salutation']
        self.app_sal_txt =  self.c['App']['salutation_text']
            

