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
        code=open('tests/data/python_sample.py').read()
        regex = re.compile("/([A-z0-9]+)$")
        a = self.app.post('/', 
            data=dict(
                code=code,
                hide="Private"
            ))
        location = a.location
        assert location
        prefix = regex.findall(location)[0]
        assert Code.find(prefix).code, code
        assert len(code) < len(self.app.get(location).data.decode('utf-8'))
        
