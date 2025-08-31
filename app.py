from flask import Flask, render_template, request, session, redirect, url_for
import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")

app = Flask(__name__)
app.secret_key = ""   # put this at the top of your file

# All of the important end points
@app.route("/", methods=["GET", "POST"])
def login():
    user_authenticated = False
    if request.method == "POST":
        # user_name = request.form["user_name"]
        email = request.form["email"]
        password = str(request.form["password"])
        # print(f"user {user_name} logged in")
        #database handling
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Hxseeb._19',
        database='calculator_web_db'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_logs;")
        all_data = cursor.fetchall()
        gmail_to_check = email
        password_to_check = password
        for i in all_data:
            if gmail_to_check == i[2] and password_to_check == i[3]:
                session["user_id"] = i[0]     # save logged in user ID
                session["user_name"] = i[1]   # save name if needed
                return redirect(url_for("home"))
        # if loop finishes with no match
        return render_template("login.html", error="No User Found, SignUp Please")
    return render_template("login.html")      

@app.route("/logout")
def logout():
    session.clear()   # clears all session data
    return redirect(url_for("login"))
 

@app.route("/home")
def home():
    if "user_id" not in session:   # check session
        return redirect(url_for("login"))
    return render_template("index.html")

@app.route("/about")
def about():
    if "user_id" not in session:
        return redirect(url_for("login"))
    return render_template("about.html")

@app.route("/history")
def history():
    # check login session first
    user_id = session.get("user_id")
    if not user_id:
        return redirect(url_for("login"))

    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Hxseeb._19',
        database='calculator_web_db'
    )
    cursor = connection.cursor()
    cursor.execute(
        "SELECT calculations, calculated_at FROM user_history WHERE user_id = %s ORDER BY calculated_at DESC LIMIT 10",
        (user_id,)
    )
    history_data = cursor.fetchall()
    print(history_data)
    cursor.close()
    connection.close()

    return render_template("history.html", history=history_data)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    user_authenticate = False
    if request.method == "POST":
        user_name = request.form["user_name"]
        email = request.form["email"]
        password = str(request.form["password"])
        #database handling 
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='Hxseeb._19',
        database='calculator_web_db'
        )
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user_logs;")
        all_data = cursor.fetchall()
        gmail_to_check = email
        password_to_check = password
        for i in all_data:
            if email == i[2]:  # already exists
                return render_template("signup.html", error_signup="User is already registered, Login")
# if loop finishes with no duplicate → insert new user
        cursor.execute(
            "INSERT INTO user_logs(name, email, password) VALUES (%s, %s, %s)",
            (user_name, email, password)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return redirect(url_for("login"))
    return render_template("signup.html")


@app.route("/calculations", methods=["POST"])
def calculations():
    expression = request.form.get("expression", "")
    button = request.form.get("btn")
    if button == "C":
        expression = ""
    elif button == "=":
        try:
            result = str(eval(expression))
            expression = result
            # save to db
            user_id = session.get("user_id")
            if user_id:
                connection = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='Hxseeb._19',
                    database='calculator_web_db'
                )
                cursor = connection.cursor()
                cursor.execute(
                    "INSERT INTO user_history (user_id, calculations) VALUES (%s, %s)",
                    (user_id, request.form.get("expression"))
                )
                connection.commit()
                cursor.close()
                connection.close()
        except:
            expression = "Error"
    else:
        expression += button
    print(expression)
    return render_template("index.html", expression_screen=expression)

if __name__ == "__main__":
    app.run(debug=True)