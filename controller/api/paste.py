
from controller.base import *

class PasteAPI(Resource,BaseAPI):

    def get(self, key=None):
        if key:
            try:
                return Response(Code.find(key).json(), 
                                mimetype="application/json")
            except:
                return self._not_found(key)
        return Response(Code.all_json(), mimetype="application/json")

    def post(self):
        req = request.get_json()
        try:
            code = Code.new(req['data'],req['private'])
            return Response(Code.find(code.key).json(), 
                            mimetype="application/json")
        except:
            return self._error()
