from flask import Flask, url_for, render_template, redirect, request
from forms import OrderForm
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
_INDEX = 0

_SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = _SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////data/order.db'
db = SQLAlchemy(app)


class CMaggi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, id, count):
        self.id = id
        self.count = count


class PMaggi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, id, count):
        self.id = id
        self.count = count


class MDosa(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=False)
    count = db.Column(db.Integer, nullable=False)

    def __init__(self, id, count):
        self.id = id
        self.count = count


@app.route('/', methods=('GET', 'POST'))
def contact():
    global _INDEX
    form = OrderForm()
    if request.method == 'POST':
        _INDEX += 1
        return redirect(url_for('order', id=_INDEX))
    else:
        return render_template('contact.html', form=form)


@app.route('/<id>')
def order(id):
    return 'Your id number is %s' % id


if __name__ == '__main__':
    db.create_all()
    db.session.commit()
    app.run(debug=True)
