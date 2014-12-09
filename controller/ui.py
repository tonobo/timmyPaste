
from flask import Response, jsonify, render_template, url_for, request, redirect
from flask.views import MethodView
from lib.core import Code, Database

class UI(MethodView):

    def get(self, key):
        if key:
            return self.__show(key)
        return render_template('index.haml')
    
    def create(self):
      return redirect(url_for('get', 
                  key=Code.new(request.form.get('code'))))

    def new(self):
        return render_template('new.haml')

    def __show(self, key):
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
    
