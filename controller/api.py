
from controller.base import *

class CodeAPI(Resource):
    def get(self, key=None):
        if key:
            try:
                return Response(Code.find(key).json(), 
                                mimetype="application/json")
            except CodeNotFound:
                error = {
                            'message': 'Cound not found such key.',
                            'requested_key': key,
                            'status': 404
                        }
                return Response(json.dumps(error, indent=4), 
                            mimetype="application/json",
                            status=404
                        )
        return Response(Code.all_json(), mimetype="application/json")

    def post(self):
        req = request.get_json()
        try:
            code = Code.new(req['data'],req['private'])
            return Response(Code.find(code).json(), 
                            mimetype="application/json")
        except:
            error = {
                      'message': 'Something went wrong. Please contact anybody.',
                      'req': req,
                      'status': 500
                    }
            return Response(json.dumps(error, indent=4), 
                             mimetype="application/json",
                             status=500)


