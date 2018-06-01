from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupFrom(Form):
	first_name = StringField('First name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last name', validators=[DataRequired("please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("please enter your email address."),Email("Please enter a valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("please enter your password."), Length(min=8,message="Use a minimum of 8 characters.")])
	submit = SubmitField('Sign up')


class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Please enter your email address."), Email("Please enter a valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password.")])
	submit = SubmitField("Sign in")

class AddressForm(Form):
  address = StringField('Address', validators=[DataRequired("Please enter an address.")])
  submit = SubmitField("Search")