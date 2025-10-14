#!/usr/bin/env python3
"""
Flask Authentication App - Main Application Entry Point

This is the main application file that creates and runs the Flask app.
Use this file to start the development server.
"""

import os
import sys
from app import create_app, db
from app.models import User

# Create the Flask application
app = create_app()

def init_db():
    """Initialize the database with tables and sample data."""
    with app.app_context():
        # Create all database tables
        db.create_all()
        
        # Check if demo user already exists
        demo_user = User.get_by_username('demo')
        if not demo_user:
            # Create a demo user for testing
            demo_user = User.create_user(
                username='demo',
                email='demo@example.com',
                password='demo123',
                first_name='Demo',
                last_name='User'
            )
            print("✅ Demo user created successfully!")
            print("   Username: demo")
            print("   Password: demo123")
        else:
            print("ℹ️  Demo user already exists")
        
        print("✅ Database initialized successfully!")

def create_admin_user():
    """Create an admin user."""
    with app.app_context():
        admin_user = User.get_by_username('admin')
        if not admin_user:
            admin_user = User.create_user(
                username='admin',
                email='admin@example.com',
                password='admin123',
                first_name='Admin',
                last_name='User'
            )
            print("✅ Admin user created successfully!")
            print("   Username: admin")
            print("   Password: admin123")
        else:
            print("ℹ️  Admin user already exists")

@app.shell_context_processor
def make_shell_context():
    """Make database and models available in Flask shell."""
    return {'db': db, 'User': User}

@app.cli.command()
def init_database():
    """Initialize the database."""
    init_db()

@app.cli.command()
def create_admin():
    """Create an admin user."""
    create_admin_user()

@app.cli.command()
def list_users():
    """List all users in the database."""
    with app.app_context():
        users = User.query.all()
        if users:
            print(f"\n📋 Found {len(users)} users:")
            print("-" * 60)
            for user in users:
                status = "✅ Active" if user.is_active else "❌ Inactive"
                print(f"ID: {user.id:2d} | {user.username:15s} | {user.email:25s} | {status}")
                print(f"     Name: {user.get_full_name():20s} | Created: {user.created_at.strftime('%Y-%m-%d %H:%M')}")
                print("-" * 60)
        else:
            print("📭 No users found in the database.")

if __name__ == '__main__':
    # Handle command line arguments
    if len(sys.argv) > 1:
        if sys.argv[1] == 'init-db':
            init_db()
            sys.exit(0)
        elif sys.argv[1] == 'create-admin':
            create_admin_user()
            sys.exit(0)
        elif sys.argv[1] == 'list-users':
            with app.app_context():
                users = User.query.all()
                if users:
                    print(f"\nFound {len(users)} users:")
                    for user in users:
                        print(f"- {user.username} ({user.email}) - {user.get_full_name()}")
                else:
                    print("No users found.")
            sys.exit(0)
    
    # Get configuration from environment variables
    debug_mode = os.environ.get('FLASK_DEBUG', 'True').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    host = os.environ.get('HOST', '127.0.0.1')
    
    print("🚀 Starting Flask Authentication App...")
    print(f"   Environment: {os.environ.get('FLASK_ENV', 'development')}")
    print(f"   Debug Mode: {debug_mode}")
    print(f"   Host: {host}")
    print(f"   Port: {port}")
    print(f"   URL: http://{host}:{port}")
    print("\n💡 Demo Credentials:")
    print("   Username: demo")
    print("   Password: demo123")
    print("\n🛑 Press Ctrl+C to stop the server")
    print("-" * 50)
    
    # Run the Flask development server
    app.run(
        host=host,
        port=port,
        debug=debug_mode,
        threaded=True
    )