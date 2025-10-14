from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from app import db

class User(UserMixin, db.Model):
    """User model for authentication."""
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False, index=True)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(200), nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    last_login = db.Column(db.DateTime)
    
    def __init__(self, username, email, password, first_name, last_name):
        """Initialize a new user."""
        self.username = username
        self.email = email
        self.set_password(password)
        self.first_name = first_name
        self.last_name = last_name
    
    def set_password(self, password):
        """Create hashed password."""
        self.password_hash = generate_password_hash(password, method='pbkdf2:sha256')
    
    def check_password(self, password):
        """Check if provided password matches hash."""
        return check_password_hash(self.password_hash, password)
    
    def get_full_name(self):
        """Return user's full name."""
        return f"{self.first_name} {self.last_name}"
    
    def update_last_login(self):
        """Update last login timestamp."""
        self.last_login = datetime.utcnow()
        db.session.commit()
    
    def is_authenticated(self):
        """Return True if user is authenticated."""
        return True
    
    def is_anonymous(self):
        """Return False as anonymous users aren't supported."""
        return False
    
    def get_id(self):
        """Return user ID as string for Flask-Login."""
        return str(self.id)
    
    def __repr__(self):
        """String representation of user."""
        return f'<User {self.username}>'
    
    @staticmethod
    def get_by_username(username):
        """Get user by username."""
        return User.query.filter_by(username=username).first()
    
    @staticmethod
    def get_by_email(email):
        """Get user by email."""
        return User.query.filter_by(email=email).first()
    
    @staticmethod
    def create_user(username, email, password, first_name, last_name):
        """Create a new user and save to database."""
        user = User(username, email, password, first_name, last_name)
        db.session.add(user)
        db.session.commit()
        return user