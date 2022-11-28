from flask import url_for
from flask import Flask

app=Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')

def login():
    return '<h1>Welcome to the login page system</h1>'


@app.route('/user/<username>')

def profile(username):

    return f'{username}\'s profile'

with app.test_request_context():

    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

if __name__=="__main__":
    app.run()

