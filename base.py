from flask import Flask, render_template
from hamlish_jinja import HamlishTagExtension


app = Flask(__name__)
app.debug = True

# add haml
app.jinja_env.add_extension(HamlishTagExtension)

@app.route('/')
def hello_word():
	return render_template('index.haml')

@app.route('/create', methods=('POST',))
def new_code():
	


if __name__ == '__main__':
    app.run(host='0.0.0.0')
