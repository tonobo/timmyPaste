
from controller.base import *

class CodeAPI(Resource):
    def get(self):
        return jsonify(entries=Database().all(False))

