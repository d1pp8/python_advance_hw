# Task 2
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page():
    return 'Hello, Flask!'

@app.route('/user/<name>')
def user(name):
    return f"Hi {name}"


if __name__ == '__main__':
    app.run()