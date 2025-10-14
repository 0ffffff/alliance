from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.forms import LoginForm, RegistrationForm
from app import db
from datetime import datetime

# Create Blueprint
main = Blueprint('main', __name__)

@main.route('/')
def index():
    """Home page route."""
    return render_template('index.html')

@main.route('/login', methods=['GET', 'POST'])
def login():
    """User login route."""
    # Redirect if user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        username_or_email = form.username_or_email.data.lower().strip()
        password = form.password.data
        
        # Try to find user by username or email
        user = User.get_by_username(username_or_email) or User.get_by_email(username_or_email)
        
        # Check if user exists and password is correct
        if user and user.check_password(password):
            if user.is_active:
                # Log in the user
                login_user(user, remember=form.remember_me.data)
                user.update_last_login()
                
                flash(f'Welcome back, {user.first_name}!', 'success')
                
                # Redirect to next page or dashboard
                next_page = request.args.get('next')
                if next_page:
                    return redirect(next_page)
                return redirect(url_for('main.dashboard'))
            else:
                flash('Your account has been deactivated. Please contact support.', 'error')
        else:
            flash('Invalid username/email or password. Please try again.', 'error')
    
    return render_template('login.html', form=form)

@main.route('/register', methods=['GET', 'POST'])
def register():
    """User registration route."""
    # Redirect if user is already authenticated
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    
    form = RegistrationForm()
    
    if form.validate_on_submit():
        try:
            # Create new user
            user = User.create_user(
                username=form.username.data.lower().strip(),
                email=form.email.data.lower().strip(),
                password=form.password.data,
                first_name=form.first_name.data.strip().title(),
                last_name=form.last_name.data.strip().title()
            )
            
            flash(f'Registration successful! Welcome, {user.first_name}!', 'success')
            
            # Automatically log in the new user
            login_user(user)
            user.update_last_login()
            
            return redirect(url_for('main.dashboard'))
            
        except Exception as e:
            db.session.rollback()
            flash('Registration failed. Please try again.', 'error')
            print(f"Registration error: {e}")  # For debugging
    
    return render_template('register.html', form=form)

@main.route('/dashboard')
@login_required
def dashboard():
    """User dashboard - protected route."""
    return render_template('dashboard.html', user=current_user)

@main.route('/profile')
@login_required
def profile():
    """User profile page."""
    return render_template('profile.html', user=current_user)

@main.route('/logout')
@login_required
def logout():
    """User logout route."""
    user_name = current_user.first_name
    logout_user()
    flash(f'You have been logged out successfully. Goodbye, {user_name}!', 'info')
    return redirect(url_for('main.index'))

@main.route('/users')
@login_required
def users():
    """Display all users - admin functionality."""
    all_users = User.query.all()
    return render_template('users.html', users=all_users)

# Error handlers
@main.errorhandler(404)
def not_found_error(error):
    """Handle 404 errors."""
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    """Handle 500 errors."""
    db.session.rollback()
    return render_template('500.html'), 500

# Context processor to make current_user available in all templates
@main.context_processor
def inject_user():
    """Make current_user available in all templates."""
    return dict(current_user=current_user)