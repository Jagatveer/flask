from flask import Flask
from werkzeug.contrib.fixers import ProxyFix
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:red'>Look Rad, No hands!! (because a simple hello world is too mainstream!)</h1>"

app.wsgi_app = ProxyFix(app.wsgi_app)

if __name__ == "__main__":
    app.run()
