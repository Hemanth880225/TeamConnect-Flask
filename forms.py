from flask_wtf import FlaskForm #flask-wtf imports the WTForms,which have inbuilt attributes for login, signup pages
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskblog.models import User
from flask_login import current_user

class RegistrationForm(FlaskForm):#FlaskForm is a special class from Flask-wtf ,lets you use WTForms easily inside flask app
    username = StringField('Username', validators= [DataRequired(), Length(min=2, max=100)]) #DataRequired: It checks that the user did not leave the field empty.
    #Length validator is used to set range of input value
    email = StringField('Email', validators=[DataRequired(), Email()])
    #Email only allows @.xyz type inputs
    password = PasswordField ('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired() , EqualTo('password')])
    #equal to helps in giving confirm_password and password should be same.
    submit = SubmitField('Sign Up') # used to create a submit form which sends the entire given data in fields to flask for validation and processing

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
           raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
           raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me') # creates a checkbox labeled 'Remember Me'
    submit = SubmitField('Login in')


class UpdateAccountForm(FlaskForm):#FlaskForm is a special class from Flask-wtf ,lets you use WTForms easily inside flask app
    username = StringField('Username', validators= [DataRequired(), Length(min=2, max=100)]) #DataRequired: It checks that the user did not leave the field empty.
    #Length validator is used to set range of input value
    email = StringField('Email', validators=[DataRequired(), Email()])
    #Email only allows @.xyz type inputs
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg','png','jpeg','webp'])])
    submit = SubmitField('Update') # used to create a submit form which sends the entire given data in fields to flask for validation and processing

    def validate_username(self, username):
       if username.data != current_user.username:
        user = User.query.filter_by(username=username.data).first()
        if user:
           raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
       if email.data != current_user.email:
        user = User.query.filter_by(email=email.data).first()
        if user:
           raise ValidationError('That email is taken. Please choose a different one.')


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')