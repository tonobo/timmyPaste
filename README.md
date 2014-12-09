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
* hamlish_jinja

Setup
----------

You could start them with gunicorn

```bash
gunicorn base:app -w 1 -b 0.0.0.0:5000
```

or easier for development.

```bash
python base.py
```





