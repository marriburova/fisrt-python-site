from flask_wtf import Form
from wtforms import StringField, BooleanField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField
from app.database import selectUsernameFromDB, selectEmailFromDB

class SignInForm(Form):
    username = StringField('username', validators = [DataRequired()])
    password = PasswordField('password', validators = [DataRequired()])
    remember_me = BooleanField('remember_me', default = False)
    
class SignUpForm(Form):
    username = StringField('Username', validators = [DataRequired()])
    email = EmailField('E-mail',validators = [Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm = PasswordField('Confirm password', validators = [DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
    
    def validate_username(self, username):
        
        cursor = selectUsernameFromDB(self)
        
        if cursor == -1:
            print('Something was wrong...')
        elif  cursor > 0:
            raise ValidationError('Please use a different username!')
    
    def validate_email(self, email):
        
        cursor = selectEmailFromDB(self)
        
        if cursor == -1:
            print('Something was wrong...')
        elif  cursor > 0:
            raise ValidationError('Please use a different email!')

     
        