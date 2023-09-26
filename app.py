from flask import Flask, render_template, flash, url_for, redirect, request
from forms import LoginForm, RegisterForm
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)


with app.app_context():
    db.create_all()


posts = [
    {
        'author': 'Cloyd Balongkit',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2023'
    },
    {
        'author': 'Raquel Balongkit',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2023'
    },
        {
        'author': 'Quinn Elize Balongkit',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2023'
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
    if form.validate_on_submit() and request.method == "POST":
        username = request.form['username']
        email = request.form['email']
        password = bcrypt.generate_password_hash(request.form['password']).decode('utf-8')
        user = User(username=username, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        flash(f"Account was created with a username of {form.username.data.title()}!", 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login",  methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit() and request.method == "POST":
        user = User.query.filter_by(email=form.email.data).first()
        if bcrypt.check_password_hash(user.password, request.form['password']):
            flash(f"Login success!", 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template("login.html", title="Login", form=form)


if __name__ == '__main__':
    app.run(debug=True)
