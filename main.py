# Import dependencies.
import datetime
import json
import uuid
import os, os.path
import cherrypy
    
# Define main class.
class MySite(object):
    @cherrypy.expose
    def index(self):
        return open('templates/index.html')

    # Define /ping service.
    @cherrypy.expose
    def ping(self):
        return json.dumps({'success': True, 'data': "pong"})

    # Define /timestamp service.
    @cherrypy.expose
    def timestamp(self):
        now = datetime.datetime.today()
        return json.dumps({'success': True, 'data': str(now)})

    # Define /uuid service.
    @cherrypy.expose
    def uuid(self):
        guid = uuid.uuid4()
        return json.dumps({'success': True, 'data': str(guid)})

    # Define /hello service.
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def hello(self):
        content = cherrypy.request.json
        msg = "Hello " + content['name'] + "!"
        return json.dumps({'success': True, 'data': msg})

    # Define /multiply service.
    @cherrypy.expose
    @cherrypy.tools.json_in()
    def multiply(self):
        content = cherrypy.request.json
        result = content['num1'] * content['num2']
        return json.dumps({'success': True, 'data': result})

# Execute app.
if __name__ == '__main__':
    conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/lib': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './static'
        }
     }    
     
    cherrypy.config.update({'server.socket_port': 5000})
    cherrypy.quickstart(MySite(), '/', conf)
