from flask import Flask,render_template,request,redirect,url_for,json,session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__,template_folder='./template')

app.secret_key = 'your secret key'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)


@app.route("/", methods = ['GET','POST'])
def login():
    msg = ''
   
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
      
        username = request.form['username']
        password = request.form['password']
    
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
       
        users = cursor.fetchone()
 
        if users:
         
            session['loggedin'] = True
            session['id'] = users['id']
            session['username'] = users['username']
            return redirect(url_for('home'))
        else:
           
            msg = 'Incorrect username/password!'

    return render_template("login.html", msg = msg)




@app.route('/index')
def home():
    return render_template("index.html")

@app.route('/signup')
def signup():
    sql = "INSERT INTO users (name, address) VALUES (%s, %s)"
    username = request.form['username']
    password = request.form['password']
    
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM users WHERE username = %s AND password = %s', (username, password,))
    # mycursor.execute(sql, val)

    # mydb.commit()

    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
