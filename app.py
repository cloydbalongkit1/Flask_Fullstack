from flask import Flask, render_template, flash, url_for, redirect
from forms import LoginForm, RegisterForm


app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"

posts = [
    {
        'author': 'Cloyd Balongkit',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Raquel Balongkit',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
        {
        'author': 'Quinn Elize Balongkit',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', title="Home", posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        flash(f"Account was created with a username of {form.username.data.title()}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",  methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f"Login success!", 'success')
        return redirect(url_for('home'))
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
