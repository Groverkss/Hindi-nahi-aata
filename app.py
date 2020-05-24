import os
from flask import Flask, url_for, render_template, redirect, request
from forms import OrderForm


app = Flask(__name__)
_INDEX = 0

_SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = _SECRET_KEY


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
    app.run(debug=True)
