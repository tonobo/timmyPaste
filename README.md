timmySyntax
===========

It representes only a poor pastbin clone.
Written in Python(3)-Flask with an SQLite backend.

![Paste](screenshot.png)

Requirements
------------

* sqlite3
* pygments
* flask
* flask-restful
* flask-classy
* hamlish_jinja

Setup
----------

You could start them with gunicorn.
There is also an systemd service / socket file shipped.
You only need to replace your WorkingDir and username. 
It will start an GUnicorn on local:9000 or ::8000.

```bash
gunicorn app:app -w 1 -b 0.0.0.0:5000
```

or easier for development.

```bash
python app.py
```





