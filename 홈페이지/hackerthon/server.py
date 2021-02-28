# library
from flask import Flask,render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
import sys

# config
DEBUG=True
FLATPAGES_AUTO_RELOAD = DEBUG

app=Flask(__name__)
app.config.from_object(__name__)
pages=FlatPages(app)
freezer=Freezer(app)

# route
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about/')
def about():
    return render_template("about.html")

@app.route('/email/')
def email():
    return render_template("email.html")

# main
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='build':
        freezer.freeze()
    else:
        app.run(port=8000)