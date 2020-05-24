from flask import Flask, url_for, render_template, redirect, request, flash
from forms import OrderForm
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

_SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = _SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/order.db'
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


db.create_all()
db.session.commit()

_INDEX = len(MDosa.query.all()) + 1


@app.route('/', methods=('GET', 'POST'))
def contact():
    global _INDEX
    form = OrderForm(request.form)
    if request.method == 'POST':
        _INDEX += 1
        os.environ['_INDEX'] = str(_INDEX)
        cmaggi = CMaggi(_INDEX, 2)
        pmaggi = PMaggi(_INDEX, 2)
        mdosa = MDosa(_INDEX, 2)

        db.session.add(cmaggi)
        db.session.add(pmaggi)
        db.session.add(mdosa)
        db.session.commit()
        return redirect(url_for('order', id=_INDEX))
    else:
        return render_template('contact.html', form=form)


@app.route('/<id>')
def order(id):
    cmaggi = CMaggi.query.filter(CMaggi.id == id).first()
    pmaggi = PMaggi.query.filter(PMaggi.id == id).first()
    mdosa = MDosa.query.filter(CMaggi.id == id).first()

    if cmaggi is None:
        cmaggi = 0
    else:
        cmaggi = cmaggi.count

    if pmaggi is None:
        pmaggi = 0
    else:
        pmaggi = pmaggi.count

    if mdosa is None:
        mdosa = 0
    else:
        mdosa = mdosa.count

    return f'ID --> {id} \n Cheese Maggi --> {cmaggi} \n Plain Maggi --> {pmaggi} \n Masala Dosa --> {mdosa}'


if __name__ == '__main__':
    app.run(debug=True)
