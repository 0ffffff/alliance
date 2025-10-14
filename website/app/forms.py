from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import (
    DataRequired, 
    Length, 
    Email, 
    EqualTo, 
    ValidationError
)
from app.models import User

class LoginForm(FlaskForm):
    """User login form."""
    username_or_email = StringField(
        'Username or Email',
        validators=[
            DataRequired(message='Username or email is required.'),
            Length(min=3, max=120, message='Username or email must be between 3 and 120 characters.')
        ],
        render_kw={"placeholder": "Enter username or email"}
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Password is required.'),
            Length(min=6, message='Password must be at least 6 characters long.')
        ],
        render_kw={"placeholder": "Enter password"}
    )
    
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    """User registration form."""
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(message='First name is required.'),
            Length(min=2, max=50, message='First name must be between 2 and 50 characters.')
        ],
        render_kw={"placeholder": "Enter first name"}
    )
    
    last_name = StringField(
        'Last Name',
        validators=[
            DataRequired(message='Last name is required.'),
            Length(min=2, max=50, message='Last name must be between 2 and 50 characters.')
        ],
        render_kw={"placeholder": "Enter last name"}
    )
    
    username = StringField(
        'Username',
        validators=[
            DataRequired(message='Username is required.'),
            Length(min=3, max=80, message='Username must be between 3 and 80 characters.')
        ],
        render_kw={"placeholder": "Choose a username"}
    )
    
    email = StringField(
        'Email',
        validators=[
            DataRequired(message='Email is required.'),
            Email(message='Please enter a valid email address.'),
            Length(max=120, message='Email must be less than 120 characters.')
        ],
        render_kw={"placeholder": "Enter email address"}
    )
    
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(message='Password is required.'),
            Length(min=6, max=200, message='Password must be between 6 and 200 characters.')
        ],
        render_kw={"placeholder": "Create a password"}
    )
    
    password_confirm = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(message='Please confirm your password.'),
            EqualTo('password', message='Passwords must match.')
        ],
        render_kw={"placeholder": "Confirm password"}
    )
    
    submit = SubmitField('Register')
    
    def validate_username(self, username):
        """Check if username is already taken."""
        user = User.get_by_username(username.data)
        if user:
            raise ValidationError('Username already taken. Please choose a different one.')
    
    def validate_email(self, email):
        """Check if email is already registered."""
        user = User.get_by_email(email.data)
        if user:
            raise ValidationError('Email already registered. Please use a different email address.')

class ChangePasswordForm(FlaskForm):
    """Change password form for authenticated users."""
    current_password = PasswordField(
        'Current Password',
        validators=[
            DataRequired(message='Current password is required.')
        ],
        render_kw={"placeholder": "Enter current password"}
    )
    
    new_password = PasswordField(
        'New Password',
        validators=[
            DataRequired(message='New password is required.'),
            Length(min=6, max=200, message='Password must be between 6 and 200 characters.')
        ],
        render_kw={"placeholder": "Enter new password"}
    )
    
    confirm_password = PasswordField(
        'Confirm New Password',
        validators=[
            DataRequired(message='Please confirm your new password.'),
            EqualTo('new_password', message='Passwords must match.')
        ],
        render_kw={"placeholder": "Confirm new password"}
    )
    
    submit = SubmitField('Change Password')