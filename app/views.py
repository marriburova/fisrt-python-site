from app import app
from flask import render_template
from .forms import SignInForm, SignUpForm 
from .database import User

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
    
@app.route('/signin', methods = ['GET', 'POST'])
def signIn():
    form = SignInForm()
    return render_template('signIn.html',
                           title = 'Sign In',
                           form = form)
    
@app.route('/signup', methods = ['GET', 'POST'])
def signUp():
    form = SignUpForm()

    if form.validate_on_submit():
        newUser = User(username = form.username.data, 
                    email = form.email.data,
                    password = form.password.data,
                    role = 0)
        result = newUser.signUpUser()
        if result == 1:
            print("Syntax error!")
        else:
            print("Registred!")
    return render_template('signUp.html',
                           title = 'Sign Up',
                           form = form)

