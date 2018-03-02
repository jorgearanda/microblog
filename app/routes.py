from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Jorge'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'I saw a rainbow and a bluejay today!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Whats up with Skycorp Studios'
        }
    ]

    return render_template('index.html', title='Home', user=user, posts=posts)
