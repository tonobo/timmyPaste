
from controller.base import *

class UrlAPI(Resource,BaseAPI):
    
    def get(self, key=None):
        try:
            if not key:
                return self._not_allowed()
            a = Url.find(key)
            if a:
                return Response(a.json(), 
                                mimetype="application/json")
            return self._not_found(key)
        except:
            return self._error()

    def post(self):
        req = request.get_json()
        try:
            url = Paste.new(req['url'])
            return Response(Url.find(url.key).json(), 
                            mimetype="application/json")
        except:
            return self._error()
