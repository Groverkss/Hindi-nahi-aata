# from flask import Flask
from flask import Flask, url_for, render_template, redirect
from forms import OrderForm


app = Flask(__name__,instance_relative_config=False)
app.config.from_object('config.Config')


@app.route('/', methods=('GET', 'POST'))
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect(url_for('qrcode'))
    return render_template('index.html', form=form)



@app.route('/<id>')
def order(id):
    return 'Your id number is %s' % id


if __name__ == '__main__':
    app.run(debug=True)
