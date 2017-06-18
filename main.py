from flask import Flask, request
import os
import jinja2

app = Flask(__name__)
app.debug = True;

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

@app.route('/')
def index():
    return "<h1>Hello World!</h1>"

app.run()
