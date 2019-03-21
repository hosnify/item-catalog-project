
from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms.fields import StringField , PasswordField , SubmitField , BooleanField  
from flask_wtf.file import FileField , FileAllowed
from wtforms.validators import DataRequired  , Email , EqualTo , ValidationError
from project2.models import User 

class RegistrationForm(FlaskForm):
    user_name= StringField('User name' , validators = [DataRequired()] )
    email= StringField('Email' , validators = [DataRequired() , Email()] )
    password= PasswordField('password' , validators = [DataRequired()] )
    confirm_password= PasswordField('confirm Password' , validators = [DataRequired() , EqualTo('password')] )
    submit= SubmitField('sign up' )
    def validate_user_name(self, user_name):
        user = User.query.filter_by(user_name=user_name.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email= StringField('Email' , validators = [DataRequired() , Email()] )
    password= PasswordField('password' , validators = [DataRequired()] )
    remember = BooleanField('Remember Me')
    submit= SubmitField('sign in' )

class UpdateProfileForm(FlaskForm):
    user_name= StringField('User name' , validators = [DataRequired() ] )
    email= StringField('Email' , validators = [DataRequired() , Email()] )
    profile_image=FileField('Upload profile picture' , validators=[FileAllowed(['png','jpg'])])
    submit= SubmitField('Save changes' )
    def validate_user_name(self, user_name):
        if user_name.data!=current_user.user_name :
            user = User.query.filter_by(user_name=user_name.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data!=current_user.email :
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
