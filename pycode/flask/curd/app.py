from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/add')
def add():
    return render_template("add.html")

@app.route('/savedetails',methods=['POST','GET'])
def savedetails():
    msg="msg"
    if request.method == 'POST':
        try:
            name=request.form['name']
            email=request.form['email']
            address=request.form['address']
            with sqlite3.connect("employee.db") as con:
                cur=con.cursor()
                cur.execute("INSERT into Employees (name, email, address) values (?,?,?)",(name,email,address)) 
                con.commit()
                msg="Employee added successfully"
        except:
            con.rollback()
            msg="Employee not added successfully"
        finally:
            return render_template("success.html",msg=msg)
            con.close()

@app.route('/view')
def view():
    con=sqlite3.connect("employee.db")
    con.row_factory=sqlite3.Row
    cur=con.cursor()
    cur.execute("select * from Employees")
    rows=cur.fetchall()
    return render_template("view.html", rows=rows)

@app.route("/delete")  
def delete():  
    return render_template("delete.html")

@app.route("/deleterecord",methods=['POST'])
def deleterecord():
    id=request.form["id"]   
    with sqlite3.connect("employee.db") as con:
        try:
            cur=con.cursor()
            cur.execute("delete from Employees where id =?",id)
            msg="Employee removed successfully"
        except:
            msg="can't be deleted"
        finally:
            return render_template("delete_result.html",msg=msg)

if __name__ == '__main__':
    app.run(host='localhost',port=8080,debug=True)