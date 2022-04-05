# save this as app.py
from flask import Flask, escape, request, url_for, redirect

app = Flask(__name__)

# url
@app.route('/')
def index():
    # redirecting to another endpoint
    return redirect(url_for('home'))

@app.route('/home')
def home():
    name = request.args.get("name", "Page")
    return f'<h1>Home {escape(name)}!</h1>'

# url/ recebe o resto como variavel e passa pra função
@app.route('/<name>')
def hello(name):
    return f'<h1>Hello, {escape(name)}!</h1>'

# printa no console
with app.test_request_context():
    print(url_for('home'))
    # url_for('nomeDaFunção', argumentos da função = 'args')
    print(url_for('hello', name='John Doe'))

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="7171")
""" flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) """