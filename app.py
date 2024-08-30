from flask import Flask,render_template,session,redirect,request,flash
from flask_mysqldb import MySQL
import yaml


app = Flask(__name__)


with open('db.yaml', 'r') as file:
    db = yaml.load(file, Loader=yaml.FullLoader)


# Configure MySQL
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

mysql = MySQL(app)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # role = request.form.get("role")

        cur = mysql.connection.cursor()
        cur.execute("SELECT username, password, FROM user WHERE username = %s AND password = %s", (username, password))
        existing_user = cur.fetchone()
        cur.close()

        if existing_user:
            session["username"] = username
            session["role_id"] = existing_user[2]

            flash("login successful")
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template("login.html")

@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        # role = request.form.get("role")

        cur = mysql.connection.cursor()
        cur.execute("SELECT username, email, password, FROM user WHERE username = %s , email = %s AND password = %s", (username, email, password))
        existing_user = cur.fetchone()
        cur.close()

        if existing_user:
            session["username"] = username

            flash("registration successful")
        else:
            flash('Invalid credentials, please try again.', 'danger')

    return render_template("register.html")






if __name__ == '__main__':
    app.run(debug=True)