from app import app
from flask import render_template
from .forms import SignInForm, SignUpForm 

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
    return render_template('signUp.html',
                           title = 'Sign Up',
                           form = form)
    