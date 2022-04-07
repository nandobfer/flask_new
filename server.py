from flask import Flask, escape, request, url_for, redirect, json

app = Flask(__name__)

# url
@app.route('/')
def index():
    # redirecting to another endpoint
    return redirect(url_for('home'))

# home page
@app.route('/home')
def home():
      
    return f'<h1>Home Page!</h1>'

# url/argument=name
@app.route('/<name>')
def hello(name):
    # print on page "Hello, argument passed on URL!"
    return f'<h1>Hello, {escape(name)}!</h1>'

# console printing
with app.test_request_context():
    print(url_for('home'))
    # url_for('functionName', functionArgs = 'args')
    print(url_for('hello', name='Fernando'))

# connection testing
@app.route('/testing_comms/', methods=['GET', 'POST'])
def data_handler():
    # requests name from client
    name = request.args.get('name')
    if name:
      test = 'Test success'
      print(f'Got connection from a client, which sent this data as name: {name}')
    else:
      test = 'Couldnt get name'
      return test
    # returns a json to client
    # return json.dumps({'name': name, 'test': test})
    # returns a string
    return f'{test}. Salve {name}'

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="7171")

""" flask run
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit) """
