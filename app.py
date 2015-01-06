from flask import Flask, Response, jsonify, render_template, url_for, request, redirect
from flask.views import MethodView
from flask.ext.restful import Api
from hamlish_jinja import HamlishTagExtension

from lib.core import Code, Database
from lib.config import Config
from controller.ui import UI
from controller.api import CodeAPI

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
app.jinja_env.add_extension(HamlishTagExtension)

def title():
    a = Config()
    a.parse()
    return a.app_title

app.jinja_env.globals.update(title=title)


Api(app).add_resource(CodeAPI, '/api/')
UI.register(app, route_base='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
