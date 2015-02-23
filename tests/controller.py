from tests.base import BaseTest
import re
from lib.code import Code

class ControllerTest(BaseTest):
    
    def test_index(self):
        a = self.app.get('/')
        assert '200 OK' == a.status

    def test_new(self):
        a = self.app.get('/new')
        assert b'textarea' in a.data
        assert b'Public' in a.data
        assert b'Private' in a.data
        assert b'_csrf_token' in a.data

    def test_redirect(self):
        code, a = self.__send_code()
        assert a.location
       
    def test_lexer(self):
        regex = re.compile("/(.+)$")
        code, a = self.__send_code()
        location = a.location
        assert location
        prefix = regex.findall(location)[0]
        lexer = self.app.get(location+'.py',
                follow_redirects=True).data.decode('utf-8')
        std = self.app.get(location,
                follow_redirects=True).data.decode('utf-8')
        no_lexer = self.app.get(location+'.pypypy',
                follow_redirects=True).data.decode('utf-8')
        assert "alert alert-danger" in no_lexer
        assert lexer != no_lexer
        assert lexer != std

    def test_url(self):
        a = self.app.post('/u/',data=dict(
            url="google.de"))
        assert "alert alert-danger" in a.data.decode('utf-8')

    def test_raw(self):
        code, a = self.__send_code(True)
        key = re.findall('value="([^"]+).+name="key"',a.data.decode('utf-8'))[0]
        assert code == self.app.get('/c/'+key+'/raw',
                follow_redirects=True).data.decode('utf-8')

    def __send_code(self, follow = False):
        code=open('tests/data/python_sample.py').read()
        a = self.app.post('/c/', 
            data=dict(
                code=code,
                hide="Private"
            ), follow_redirects=follow)
        return (code, a)

        
