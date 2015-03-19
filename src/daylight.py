from flask import Flask, render_template
from livereload import Server
from sassutils.wsgi import SassMiddleware

app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        'daylight': ('static/sass', 'static/css', '/static/css')
    })
    server = Server(app.wsgi_app)
    server.serve(port=5000, host='0.0.0.0')
    #app.run()
