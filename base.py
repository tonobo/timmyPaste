from flask import Flask, Response, render_template, url_for, request, redirect
from flask.views import MethodView
from hamlish_jinja import HamlishTagExtension
from core import Code

app = Flask(__name__)
app.debug = True
app.jinja_env.add_extension(HamlishTagExtension)

@app.route('/')
def index():
	return render_template('index.haml')

@app.route('/new', methods=('GET',))
@app.route('/create', methods=('POST',))
def new_code():
    if request.method == "GET":
        return render_template('new.haml')
    else:
        key = Code.new(request.form.get('code'))
        return redirect(url_for('show', key=key))

@app.route('/<key>/raw')
def raw(key):
    return Response(Code.find(key).code, mimetype='text/plain')
    
@app.route('/<key>')
def show(key):
    keylist=key.split('.')
    ckey = ((key,'txt'),keylist)[bool(len(keylist)>1)]
    a = Code.find(ckey[0])
    try: 
        hcode = a.highlight('.'+ckey[1])
        flash=False
    except:
        hcode = a.highlight('.txt')
        flash="""
            Sorry, but the Lexxer doesn't exist. Please enter only filename
            suffix like .rb or .py
        """
    return render_template('show.haml',
                key=ckey[0],
                flash=flash,
                code=hcode)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
