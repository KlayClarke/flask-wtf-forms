import os
from flask_wtf import FlaskForm
from flask_bootstrap import Bootstrap
from flask import Flask, render_template, request
from wtforms.validators import DataRequired, Email, Length
from wtforms import StringField, PasswordField, SubmitField


app = Flask(__name__)
Bootstrap(app)

app.secret_key = os.environ.get('FLASK_SECRET_KEY')


class LoginForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8)])
    login_button = SubmitField('Login')


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    form.validate_on_submit()
    if request.method == 'POST' and form.validate_on_submit():
        print(form.email.data)
        print(form.password.data)
        return render_template('success.html')
    return render_template('login.html', form=form)


@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/denied')
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)
