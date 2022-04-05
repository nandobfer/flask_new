# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
""" flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) """