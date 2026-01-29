"""
Basic Flask Web Application with Navigation
============================================
A simple web app with Home, About, and Contact pages.
Debug mode is enabled for development purposes.
"""

from flask import Flask, render_template, request

app = Flask(__name__)

# Enable debug mode for verbose error messages and stack traces
app.config['DEBUG'] = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


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
    # Run in debug mode with verbose error messages
    app.run(debug=True, host='0.0.0.0', port=5000)
