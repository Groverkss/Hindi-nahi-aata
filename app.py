from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/<id>')
def order(id):
    return 'Your id number is %s' % id


if __name__ == '__main__':
    app.run(debug=True)
