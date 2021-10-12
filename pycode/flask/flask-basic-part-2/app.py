from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return "Hello World"


if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)