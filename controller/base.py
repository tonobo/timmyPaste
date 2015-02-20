
from flask import Response, jsonify, render_template, url_for, request, redirect
from flask.ext.restful import Resource
from flask.ext.classy import FlaskView, route
from flask.ext.babel import gettext, ngettext
from lib.code import Code
from lib.url import Url
from lib.config import Config
import json

class BaseAPI:

    def _not_found(self, key):
        error = {
                    'message': 'Could not found such key.',
                    'requested_key': key,
                    'status': 404
                }
        return Response(json.dumps(error, indent=4), 
                    mimetype="application/json",
                    status=404
                )
    
    def _not_allowd(self):
        error = {
                  'message': 'Method not allowed',
                  'status': 400
                }
        return Response(json.dumps(error, indent=4), 
                         mimetype="application/json",
                         status=400)

    def _error(self):
        error = {
                  'message': 'Something went wrong. Please contact anybody.',
                  'status': 500
                }
        return Response(json.dumps(error, indent=4), 
                         mimetype="application/json",
                         status=500)



class BaseController:
    
    def config(self):
        a = Config()
        a.parse()
        return a
