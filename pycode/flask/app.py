from markupsafe import escape
from flask import Flask, abort, redirect, url_for, render_template

app=Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")
@app.route('/index/')
def hello():
  return '<h1>Hello World</h1>'

@app.route('/about/')
def about():
  return '<h3> this is Flask web app</h3>'

@app.route('/contacts/')
def contacts():
  return '<h2>this is contacts page </h2>'

@app.route('/capitalize/<word>/')
def capitalize(word):
    return '<h1>{}</h1>'.format(escape(word.capitalize()))

@app.route('/add/<int:n1>/<int:n2>/')
def add(n1,n2):
  return '<h1>{}</h1>'.format(n1+n2)

@app.route('/users/<int:user_id>/')
def greet_users(user_id):
  users = ['Sunil','Ganesh','Ram']
  try:
    return '<h2>Hi {}</h2>'.format(users[user_id])
  except IndexError:
    abort(404)

@app.route('/admin')
def admin():
  return 'Hello Admin'

@app.route('/guest/<guest>')
def guest(guest):
  return 'Hello %s as guest' %guest

@app.route('/user/<name>')
def hello_user(name):
  if name == 'admin': 
    return redirect(url_for('admin'))
  else:
    return redirect(url_for('guest', guest = name))
