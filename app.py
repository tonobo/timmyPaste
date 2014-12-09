from flask import Flask, Response, jsonify, render_template, url_for, request, redirect
from flask.views import MethodView
from flask.ext.restful import Api
from hamlish_jinja import HamlishTagExtension

from lib.core import Code, Database
from controller.ui import UI
from controller.api import CodeAPI

app = Flask(__name__)
app.debug = True
app.jinja_env.add_extension(HamlishTagExtension)

rest = Api(app)
rest.add_resource(CodeAPI, '/api/')
ui = UI.as_view('ui')
app.add_url_rule('/', view_func=ui)
app.add_url_rule('/<string:key>', view_func=ui)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
