
from controller.base import *
import re

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
        u = url if re.match('^(https?|ftps?|rsync)://',url) else 'http://'+url
        key = Url.new(u)
        return render_template('new.haml', 
                flash=gettext("""
                    Url redirection setup %(url)s
                    Your short URL: http://%(app)s/%(key)s""",
                    url=url, key=key, app=self.config().url))

