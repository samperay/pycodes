from flask import Flask, render_template, url_for, redirect, request, make_response, abort

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

# you need to open 'userlogin.html' from webbrowser and then click on 'submit' button
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

# static files 
@app.route('/index')
def index():
    return render_template('index.html')

# flask request object 

# Form − It is a dictionary object containing key and value pairs of form parameters and their values.
# args − parsed contents of query string which is part of URL after question mark (?).
# Cookies − dictionary object holding Cookie names and values.
# files − data pertaining to uploaded file.
# method − current request method.

# student results 

@app.route('/student')
def student():
    return render_template('student.html')
app.add_url_rule('/student/','/student',student)

@app.route('/student_results',methods=['POST','GET'])
def student_results():
    if request.method=='POST':
        result = request.form
        return render_template("student_results.html",result=result)

# flask re-direct and errors handling 
# Flask.redirect(location, statuscode, response)
    # localtion - parameter in the url, where response should be re-directed. 
    # statuscode - browser's defaults to 302 
    # respone - parameter used to instantiate response 

    # HTTP_300_MULTIPLE_CHOICES
    # HTTP_301_MOVED_PERMANENTLY
    # HTTP_302_FOUND   ==> Defautl
    # HTTP_303_SEE_OTHER
    # HTTP_304_NOT_MODIFIED
    # HTTP_305_USE_PROXY
    # HTTP_306_RESERVED
    # HTTP_307_TEMPORARY_REDIRECT

    # Flask.abort(code)

    # 400 − Bad Request
    # 401 − Unauthenticated
    # 403 − Forbidden
    # 404 − Not Found
    # 406 − Not Acceptable
    # 415 − Unsupported Media Type
    # 429 − Too Many Requests

@app.route('/logins')
def logins():
    return render_template('logins.html')

@app.route('/adminlogin',methods=['POST','GET'])
def userlogins():
    if request.method=='POST' and request.form['username'] == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        abort(403)




if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)
