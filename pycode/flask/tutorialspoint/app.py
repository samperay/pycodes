from flask import Flask, render_template, url_for, redirect, request

app=Flask(__name__)

# In the below, when you try to hit the URL from the browser, "/hello" would be working fine, but it doesn't when "/hello/" is being hit. In order to sort of these issues, we would be using "url_for"

@app.route('/hello')
def hello():
    return "<html><h1>Hello World</h1></html>"

# kind of alias for /hello or /, it would by default calls up /hello function
app.add_url_rule('/','hello',hello)

# defaults to string
@app.route('/hello/<name>')
def hello_params(name):
    #return "Hello {}".format(name)
    return render_template('hello.html', user=name)

# we can also pass - int, float, path to the parameters 

@app.route('/blog/<int:postid>')
def show_blog(postid):
    return "Post ID: {}".format(postid)

@app.route('/rev/<float:revno>')
def revision(revno):
    return "Revision {}".format(revno)

# url_for urls 
@app.route('/admin')
def hello_admin():
    return "Hello Admin !!, Welcome"

@app.route('/guest/<guest>')
def hello_guest(guest):
    return "Hello Guest {}".format(guest)

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

# if you need to render data into html, then you might be required to use the jinja templates.

# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements

@app.route('/user/<int:score>')
def hello_score(score):
    return render_template('score.html',marks=score)

# HTTP protocol using flask. 
# GET - Default method, most commonly used 
# HEAD - same as GET, but with no response body 
# POST - send HTML from data to server 
# PUT - replace current representations of the target with uploaded content 
# DELETE - removes the representation of the target resource. 

@app.route('/userlogin', methods=['POST','GET'])
def userlogin():
    if request.method=='POST':
        user=request.form['user']
        if user == 'admin':
            return redirect(url_for('hello_admin'))
        else:
            return redirect(url_for('hello_guest',guest=user))

# student results 
@app.route('/result')
def result():
    dict = {'phy':'50',
            'che':'60',
            'mat':'70'
            }
    return render_template('result.html',result=dict)

if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)
