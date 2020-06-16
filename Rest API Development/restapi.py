from flask import Flask

app = Flask(__name__)

@app.route('/func')
def func():
    return 'Hello World'

@app.route('/bye')
def bye():
    return 'bye bye'

# Port 5000-6000 are available for public use

app.run(port=5000)