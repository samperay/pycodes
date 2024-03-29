from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/about')
def about():
    return 'About'


if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True)
