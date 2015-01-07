
from controller.base import *

class UI(FlaskView,BaseController):

    def index(self):
        return render_template('index.haml')

    def get(self, key=None):
        try: 
            flash=None
            if key == 'new':
                return render_template('new.haml')
            elif key:
                return self.__show(key)
        except CodeNotFound:
            flash=gettext("Code not found.")
        return render_template('new.haml', flash=flash)

    @route('/<key>/raw')
    def raw(self, key):
        return Response(Code.find(key).code, mimetype="text/plain")
    
    def post(self):
        try:
            hide = (True,False)[bool(request.form.get('hide') == 'true')]
            return redirect('/'+Code.new(request.form.get('code'), hide))
        except:
            return render_template('new.haml', 
                    flash=gettext('Could not create the code.'))

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
    
