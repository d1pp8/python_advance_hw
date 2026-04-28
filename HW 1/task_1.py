#Task 1
#Example code from the task
from flask import Flask

app = Flask(__name__)

#The main error we have is in routing, must be like "('/') - root route" or another one...
@app.route(")
def home():
    return "Hello, World!"

if __name__ == '__main__':
    app.run()