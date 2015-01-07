from flask import Flask, Response, jsonify, render_template, url_for, request, redirect
from flask.views import MethodView
from flask.ext.restful import Api
from flask.ext.babel import Babel
from hamlish_jinja import HamlishTagExtension

from lib.core import Code, Database
from lib.config import Config
from controller.ui import UI
from controller.api import CodeAPI

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
app.jinja_env.add_extension(HamlishTagExtension)
babel = Babel(app)

conf = Config()
conf.parse()

app.config['BABEL_DEFAULT_LOCALE'] = conf.app_locale

Api(app).add_resource(
        CodeAPI, 
        '/api/',
        '/api/<key>')

UI.register(app, route_base='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
