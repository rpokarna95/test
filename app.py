"""
Basic Flask Web Application with Navigation
============================================
A simple web app with Home, About, and Contact pages.
"""

import os
from flask import Flask, render_template, request

app = Flask(__name__)

# Security: Load configuration from environment variables
# NEVER enable debug mode in production - it exposes sensitive information
# and enables the Werkzeug debugger console which allows arbitrary code execution
app.config['DEBUG'] = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
app.config['TEMPLATES_AUTO_RELOAD'] = app.config['DEBUG']

# Security: SECRET_KEY is required for session security and CSRF protection
# Generate a secure key with: python -c "import secrets; print(secrets.token_hex(32))"
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', os.urandom(32).hex())


@app.route('/')
def home():
    """Render the home/landing page."""
    return render_template('home.html', active_page='home')


@app.route('/about')
def about():
    """Render the about page."""
    return render_template('about.html', active_page='about')


@app.route('/contact')
def contact():
    """Render the contact page."""
    return render_template('contact.html', active_page='contact')


if __name__ == '__main__':
    # Security: Debug mode controlled by environment variable (defaults to False)
    # In production, use a proper WSGI server like Gunicorn instead of Flask's dev server
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    host = os.environ.get('FLASK_HOST', '127.0.0.1')  # Default to localhost for security
    port = int(os.environ.get('FLASK_PORT', '5000'))
    app.run(debug=debug_mode, host=host, port=port)
