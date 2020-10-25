from flask import Flask, render_template, redirect, url_for
from forms import CovidForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "TWOJA-STARA-SECRET"


@app.route('/', methods=('GET', 'POST'))
def hello_world():
    form = CovidForm()
    if form.validate_on_submit():
        return redirect(url_for('/owned'))
    return render_template("index.html", form=form)

@app.route('/owned', methods=['GET', 'POST']) 
def owned():
    return render_template("owned.html")

if __name__ == '__main__':
   app.run()