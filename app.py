from flask import Flask, session, render_template, abort, request, redirect
from flask.views import MethodView
from flask.ext.restful import Api
from flask.ext.babel import Babel
from hamlish_jinja import HamlishTagExtension
import random, string, re

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


app.config['SECRET_KEY'] = 'PdqXX7K5MTfpAK635&$&d2NuYB014&P7Emybbk8DWj&$COA8KzDn9N%9mml58TSWu:667'
app.config['BABEL_DEFAULT_LOCALE'] = conf.app_locale

Api(app).add_resource(PasteAPI, '%s/pa/' % (conf.path_prefix,), '%s/pa/<key>' % (conf.path_prefix,))
Api(app).add_resource(UrlAPI, '%s/ua/<key>' % (conf.path_prefix,))

@app.before_request
def csrf_protect():
    if request.method == "POST" and not app.testing:
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)

def generate_csrf_token():
    if '_csrf_token' not in session:
        k = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(100))
        session['_csrf_token'] = k
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token
app.jinja_env.globals['path_prefix'] = conf.path_prefix


@app.route('%s/' % (conf.path_prefix,))
def render_new():
    return render_template('new.haml')

@app.route('%s/<key>' % (conf.path_prefix,))
def redirect_site(key = None):
    try: 
        if key:
            keys = re.findall('([^\.]+)',key)
            a=Key().find(keys[0])
            return redirect('%s/%s/%s' % (conf.path_prefix, a[2][0].lower(),key,))
        return render_template('index.haml')
    except:
        abort(404)


PasteUtil.register(app, route_base='%s/c/' % (conf.path_prefix,))
UrlShorten.register(app, route_base='%s/u/' % (conf.path_prefix,))


if __name__ == '__main__':
    app.run(host='0.0.0.0')
