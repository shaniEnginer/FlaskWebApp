from flask_wtf import FlaskForm
from flask_wtf.file import FileField , FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField , TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo ,ValidationError
from flaskblog.models import User

#  Registration form class
class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user= User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That email is already take !')

    def validate_email(self, email):
        email= User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('That email is already take !')


#  login Form Class 
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



# Update Form calss 
class UpdateForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture= FileField('Update profile picture' , validators=[FileAllowed(['png' , 'jpg'])])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user= User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That email is already take !')

    def validate_email(self, email):
        if email.data != current_user.email:
            email= User.query.filter_by(email=email.data).first()
            if email:
                raise ValidationError('That email is already take !')

#  Defing form for the Post creation
class PostForm(FlaskForm):
    title= StringField('title' , validators=[DataRequired() , Length(min=5 , max=30)])
    content = TextAreaField('content' , validators=[DataRequired()])
    submit= SubmitField('Post')
