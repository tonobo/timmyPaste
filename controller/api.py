
from flask import Response, jsonify, render_template, url_for, request, redirect
from flask.ext.restful import Resource
from lib.core import Database

class CodeAPI(Resource):
    def get(self):
        return jsonify(entries=Database().all())

