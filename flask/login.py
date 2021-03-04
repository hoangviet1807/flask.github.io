from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__,template_folder='./template')

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flask'

mysql = MySQL(app)

@app.route('/')
def Home():
     cur = mysql.connection.cursor()
     cur.execute("select * from users")
     fetchdata = cur.fetchall()
     cur.close()
     return render_template('home.html', data=fetchdata)

if __name__ == "__main__":
    app.run(debug = True)