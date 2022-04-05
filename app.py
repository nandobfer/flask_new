# save this as app.py
from flask import Flask, escape, request

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "Page")
    return f'<h1>Home, {escape(name)}!</h1>'

@app.route('/about')
def about():
    # name = request.args.get("name", "Page")
    return f'<h1>About Page!</h1>'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="7171")
""" flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) """