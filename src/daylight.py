from flask import Flask, render_template
from livereload import Server
app = Flask(__name__)

@app.route('/')
def hello_world(name=None):
    return render_template('index.html')

if __name__ == '__main__':
    app.debug = True
    server = Server(app.wsgi_app)
    server.serve(port=5000, host='127.0.0.1')
    #app.run()
