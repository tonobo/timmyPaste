
from controller.base import *

class UrlShorten(FlaskView,BaseController):

    def get(self, key=None):
        try: 
            flash=None
            if key == 'new':
                return render_template('urlshorten_new.haml')
            elif key:
                u=Url.find(key)
                return redirect(u.url, code=302)
        except:
            flash=gettext("Url not found.")
        return render_template('urlshorten_new.haml', flash=flash)

    def post(self):
        url = request.form.get('url')
        key = Url.new(url)
        return render_template('urlshorten_new.haml', 
                flash=gettext("""
                    Url redirection setup %(url)s
                    Your short URL: http://%(app)s/u/%(key)s""",
                    url=url, key=key, app=self.config().url))

