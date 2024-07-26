from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<p>I am root!</p><p>/who</p>'

@app.route('/who')
def test():
    return '<p>I am who?</p>'

if __name__ == "__main__":
    app.run()