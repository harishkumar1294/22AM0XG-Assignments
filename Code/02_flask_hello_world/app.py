from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World! ' + 'Harish Kumar A ' + '7376222IT147 ' + 'Dept of IT'

if __name__ == '__main__':
    app.run(debug=True)