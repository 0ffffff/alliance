# Flask Full-Stack Authentication App

A complete full-stack web application built with Python Flask featuring user authentication, session management, and a responsive user interface.

## Features

- User Registration and Login
- Secure Password Hashing
- Session Management with Flask-Login
- Form Validation with Flask-WTF
- Responsive Design
- SQLite Database Integration
- Protected Routes
- User Dashboard

## Tech Stack

- **Backend**: Python Flask
- **Database**: SQLite with Flask-SQLAlchemy
- **Authentication**: Flask-Login
- **Forms**: Flask-WTF
- **Frontend**: HTML5, CSS3, JavaScript
- **Password Security**: Werkzeug password hashing

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd flask-auth-app
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set up Environment Variables
Create a `.env` file in the root directory:
```
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///app.db
FLASK_ENV=development
```

### Step 5: Initialize Database
```bash
python run.py init-db
```

### Step 6: Run the Application
```bash
python run.py
```

The application will be available at `http://localhost:5000`

## Project Structure

```
flask-auth-app/
├── app/
│   ├── __init__.py          # Flask app factory
│   ├── models.py            # Database models
│   ├── routes.py            # Application routes
│   ├── forms.py             # WTForms forms
│   ├── templates/           # HTML templates
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── login.html
│   │   ├── register.html
│   │   └── dashboard.html
│   └── static/              # Static files
│       ├── css/
│       │   └── style.css
│       └── js/
│           └── main.js
├── config/
│   └── config.py            # Configuration settings
├── app.py                   # Main application file
├── run.py                   # Application runner
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables
├── .gitignore              # Git ignore file
└── README.md               # This file
```

## Usage

1. **Home Page**: Navigate to `http://localhost:5000` to see the welcome page
2. **Register**: Create a new account at `/register`
3. **Login**: Sign in to your account at `/login`
4. **Dashboard**: Access your protected dashboard after logging in
5. **Logout**: Use the logout link to end your session

## Security Features

- Password hashing using Werkzeug's secure methods
- CSRF protection with Flask-WTF
- Session-based authentication
- Input validation and sanitization
- SQL injection protection with SQLAlchemy ORM

## API Endpoints

- `GET /` - Home page
- `GET|POST /login` - User login
- `GET|POST /register` - User registration
- `GET /dashboard` - Protected user dashboard
- `GET /logout` - User logout

## Development

To run in debug mode:
```bash
export FLASK_ENV=development
python run.py
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For questions or issues, please open an issue on the repository or contact the maintainer.