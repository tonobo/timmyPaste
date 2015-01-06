from tests.base import BaseTest
import re
from lib.core import Code

class ControllerTest(BaseTest):
    
    def test_index(self):
        a = self.app.get('/')
        assert b'TimmySyntax' in a.data

    def test_new(self):
        a = self.app.get('/new')
        assert b'textarea' in a.data
        assert b'Public' in a.data
        assert b'Private' in a.data

    def test_create_and_show(self):
        code, a = self.__send_code()
        regex = re.compile("/([A-z0-9]+)$")
        location = a.location
        assert location
        prefix = regex.findall(location)[0]
        assert Code.find(prefix).code, code
        assert len(code) < len(self.app.get(location).data.decode('utf-8'))
       
    def test_lexer(self):
        regex = re.compile("/([A-z0-9]+)$")
        code, a = self.__send_code()
        location = a.location
        assert location
        prefix = regex.findall(location)[0]
        lexer = self.app.get(location+'.py').data.decode('utf-8')
        std = self.app.get(location).data.decode('utf-8')
        no_lexer = self.app.get(location+'.pypypy').data.decode('utf-8')
        assert "Lexxer doesn't exist." in no_lexer
        assert lexer != no_lexer
        assert lexer != std

    def test_raw(self):
        code, a = self.__send_code()
        assert code == self.app.get(a.location+'/raw').data.decode('utf-8')

    def __send_code(self):
        code=open('tests/data/python_sample.py').read()
        a = self.app.post('/', 
            data=dict(
                code=code,
                hide="Private"
            ))
        return (code, a)

        
