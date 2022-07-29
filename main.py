from flask import Flask, render_template, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField
from flask_bootstrap import Bootstrap
import os


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[validators.Length(max=30, min=5), validators.Email()])
    password = PasswordField('Password', validators=[validators.Length(max=30, min=8)])
    submit = SubmitField('Log In')


app = Flask(__name__)
Bootstrap(app)
app.secret_key = os.environ.get('KEY')
email = ''
password = ''


@app.route("/")
def home_page():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login_page():
    global email, password
    form = LoginForm()
    if form.validate_on_submit():
        email1 = form.email.data
        password1 = form.password.data
        if email1 == 'admin@email.com' and password1 == '12345678':
            return render_template('success.html')
        else:
            return render_template('denied.html')
        # print(f'Email: {email1}')
        # print(f"Password: {password1}")
        # return redirect(url_for('home_page'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
