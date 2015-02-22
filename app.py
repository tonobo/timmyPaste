from flask import Flask, Response, jsonify, render_template, url_for, request, redirect
from flask.views import MethodView
from flask.ext.restful import Api
from flask.ext.babel import Babel
from hamlish_jinja import HamlishTagExtension

from lib.db.key import Key

from lib.config import Config

from controller.paste_util import PasteUtil
from controller.url_shorten import UrlShorten
from controller.api import *

app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True
app.jinja_env.add_extension(HamlishTagExtension)
babel = Babel(app)

conf = Config()
conf.parse()

app.config['BABEL_DEFAULT_LOCALE'] = conf.app_locale

Api(app).add_resource(PasteAPI, '/pa/', '/pa/<key>')
Api(app).add_resource(UrlAPI, '/ua/<key>')

@app.route('/new')
def render_new():
    return render_template('new.haml')

@app.route('/<key>')
def redirect_site(key):
    try: 
        a=Key().find(key)
        return redirect('/%s/%s' % (a[2][0].lower(),key,))
    except Key.KeyNotFound:
        abort(404)


PasteUtil.register(app, route_base='/c/')
UrlShorten.register(app, route_base='/u/')


if __name__ == '__main__':
    app.run(host='0.0.0.0')
