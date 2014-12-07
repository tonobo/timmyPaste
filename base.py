from flask import Flask, render_template, url_for, request
from hamlish_jinja import HamlishTagExtension
from core import Code

app = Flask(__name__)
app.debug = True

# add haml
app.jinja_env.add_extension(HamlishTagExtension)

@app.route('/')
def hello_word():
	return render_template('index.haml')

@app.route('/new', methods=('GET',))
@app.route('/create', methods=('POST',))
def new_code():
    if request.method == "GET":
        return render_template('new.haml')
    else: 
        key = Code.new(request.args.get('code', ''))
        return redirect(url_for('show', key=key))

@app.route('/show/<key>')
def show(key):
    keylist=key.split('.')
    if len(keylist) > 1:
        a = Code.find(keylist[0])
        return render_template('show.haml', 
                code=a.highlight(a[1]), 
                raw=False)
    else:
        a = Code.find(key)
        render_template('show.haml', 
                code=a.code,
                raw=True)
    


if __name__ == '__main__':
    app.run(host='0.0.0.0')
