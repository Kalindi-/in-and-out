
import os
import webapp2
import jinja2
import urllib

from google.appengine.ext import ndb


#initializing work environment: the file, and the jinja
template_dir = os.path.join(os.path.dirname(__file__), "templates")
template_loader = jinja2.FileSystemLoader(template_dir)
template_env = jinja2.Environment(loader = template_loader, autoescape = True)

# page making handler
class Handler(webapp2.RequestHandler):
    """contains the basic methods for rendering the templates into html pages"""
    def write(self, *arguments, **key_word_dictionary):
        """makes a html page out of the inputs"""
        self.response.out.write(*arguments, **key_word_dictionary)

    def render_str(self, template, **parameters):
        """makes a string out of the inputs"""
        t = template_env.get_template(template)
        return t.render(parameters)

    def render(self, template, **key_word_dictionary):
        """takes template to fill it in with the keywords"""
        self.write(self.render_str(template, **key_word_dictionary))


#comments
class Comment(ndb.Model):
    """comments"""
    comment = ndb.StringProperty()
    amail = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)


#my click objects
class Click(ndb.Model):
    """who comes"""
    country = ndb.StringProperty()
    date = ndb.DateTimeProperty(auto_now_add=True)



class Page(Handler):
    def get(self):
        """makes pages up"""
        thanks = self.request.get('thanks')
        error = self.request.get('error')
        self.render("index.html", thanks=thanks, error=error)

    def post(self):
        """retrieve where from"""
        country = self.request.get('country')
        click = Click(country=country)
        click.put()

        """retrieve input data and create instances of object Comment"""
        comment = self.request.get('comment')
        email = self.request.get('email')

        if (comment and comment.isspace() == False) or (email and email.isspace() == False):
            comment = Comment(comment=comment, amail=email)
            comment.put()
            url_info = {'thanks': True}
            self.redirect('/?' + urllib.urlencode(url_info)+ '&#comment')
        else:
            url_info = {'error': True}
            self.redirect('/?' + urllib.urlencode(url_info) + '&#comment')



#creation of pages
app = webapp2.WSGIApplication([('/', Page)], debug = True)