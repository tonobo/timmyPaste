
from controller.base import *

class PasteUtil(FlaskView,BaseController):

    def index(self):
        return render_template('index.haml')

    def get(self, key):
        try: 
            flash=None
            return self.__show(key)
        except:
            flash=gettext("Code not found.")
        return render_template('new.haml', flash=flash)

    @route('/<key>/raw')
    def raw(self, key):
        return Response(Code.find(key).code, mimetype="text/plain")
    
    def post(self):
        if len(request.form) > 1:
            code = request.form.get('code')
            hide = (True,False)[bool(request.form.get('hide') == 'true')]
            return redirect('/'+Code.new(code, hide))
        elif request.json: 
            code = request.json.get('code')
            hide = request.json.get('hide')
            return redirect('/ca/'+Code.new(code,hide))
        else:
            return Response("http://%s/%s\n" % (self.config().url,
                Code.new(list(request.form)[0],
                    self.config().paste_default_hidden)), 
                mimetype="text/plain")

    def __show(self, key):
      keylist=key.split('.')
      ckey = ((key,'txt'),keylist)[bool(len(keylist)>1)]
      a = Code.find(ckey[0])
      try: 
        hcode = a.highlight('.'+ckey[1])
        flash=False
      except:
        hcode = a.highlight('.txt')
        flash=gettext("Can't find lexxer.")
      return render_template('show.haml',
                key=ckey[0],
                flash=flash,
                code=hcode)    
   
