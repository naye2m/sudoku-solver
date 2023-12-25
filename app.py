# from flask import Flask, render_template, url_for, request, redirect, session
# # from flask_sqlalchemy import SQLAlchemy
# from cs50 import SQL
# from flask_session import session
# from werkzeug.security import check_password_hash, generate_password_hash
import os

from cs50 import SQL
from flask import (
    Flask,
    flash,
    redirect,
    render_template,
    request,
    session,
    jsonify,
    Response,
)
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from markupsafe import escape
import re, subprocess, json

from helpers import apology, login_required

# . before deploy
debug = {"isOn": False}
#   app.run(debug=True)> app.run()

# cs50 flask flask_session werkzeug.security markupsafe

app = Flask(__name__)
app.secret_key = "your_secret_key"
db = SQL("sqlite:///test.db")
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql//username:pass@localhost/wordle.db'
# db = SQLAlchemy(app)
# db.execute("create table users")
# import mysql.connector
# print(db.execute('select * from ss_users'))
# mydb = mysql.connector.connec(
#     host='localhost',
#     user='',
#     passwd = 'psswrd'
#     )
# sqlCursor = mydb.cursor()
# myc = sqlCursor
# myc.execute("create Database wordle")
# myc.execute("show database")
# def sqlE(command = ''):
#     if command == '': return
#     return mydb.cursor().execute(command)


# class user (db.model):
#     id = db.Column(db.Integer, primary_key = True)
#     userName = db.Column(db.String(20), nullable = False)
#     YoB = db.Column(db.Integer, default= 0)
#     dateOfCreation = db.Column(db.dateTime, default= datetime.utcnow)

# def __repr__(self):
#     return self.id
if __name__ == "__main__":
    app.run(
        debug=debug["isOn"]
    )
##_____________________________________debug = false____________________________________


# . -----------------------------------------------------------------------------------------------------------------
# . ------------------------------------------------appZone----------------------------------------------------------
# . -----------------------------------------------------------------------------------------------------------------
# <-------------------------- games zone
# <<------------------------------------------- application zone----------------------------------------------------->>
def ckToken(token):
    return token == 2024
@app.route("/api/ss", methods=["POST", "GET"])
@app.route("/api/solvesudoku", methods=["POST", "GET"])
@login_required
def solveSudokuApi():
    if request.method == "GET":
        # print(request.args.get("sudoku"))
        if request.args.get("sudoku") == None:
            # return jsonify(response = {"m":"wrong usage no fuild find named sudoku"}, status=403, mimetype='application/json')
            return Response(
                response=json.dumps(
                    {
                        "massage": "Error: while getting data",
                        "Error": "Dosen't contain arg 'sudoku'",
                    }
                ),
                status=400,
                mimetype="application/json",
            )
        if len(request.args.get("sudoku")) == 81:
            us = request.args.get("sudoku")
            if not isStrOnlyContainDigits(us):
                return Response(
                    response=json.dumps(
                        {
                            "massage": "Error: while getting data",
                            "Error": "Dosen't contain Digit in 'sudoku <size : 81>'",
                        }
                    ),
                    status=400,
                    mimetype="application/json",
                )
        else:
            return Response(
                response=json.dumps(
                    {
                        "massage": "Error: while getting data",
                        "Error": "Dosen't contain arg 'sudoku <size : 81>'",
                    }
                ),
                status=400,
                mimetype="application/json",
            )
        if(session["user_id"]):
            user = session["user_id"]
        elif(ckToken(request.args.get("token"))):
            user = request.args.get("token")
        else:
            return Response(
                response=json.dumps(
                    {
                        "massage": "Error: Access Denied",
                        "Error_from_terminal": result[1],
                    }
                ),
                status=455,
                mimetype="application/json",
            )

        c_file_path = "c_files/ss"
        # result = run_in_ter("./"+c_file_path+" 090600800000503400807000610000050007000790100000006300070000020040000000203061784" ).stdout.decode().split("\n")
        clistr = f"./{c_file_path} {us}"
        result = run_in_ter(clistr)
        if result[0] == 0:
            result = result[1]
        else:
            return Response(
                response=json.dumps(
                    {
                        "massage": "Error: while getting data from terminal",
                        "Error_from_terminal": result[1],
                    }
                ),
                status=403,
                mimetype="application/json",
            )
        result = result.stdout.decode().split("\n")

        # pstr sstr date user_id id complexity_in_backtrack
        # return jsonify(
        #     {"massage": "wrong usage"}, status=403, mimetype="application/json"
        # )
        db.execute(
            'INSERT INTO "history_for_ss" ("user_id","problem_str","solved_str","complexity_in_backtrack") VALUES (?,?,?,?)',
            user,
            us,
            result[0],
            result[1],
        )
        return jsonify(
            {
                "massage": "Done",
                "input": us,
                "result": result[0],
                "complexity_in_backtrack": result[1],
            }
        )


@app.route("/", methods=["POST", "GET"])
@app.route("/solve_sudoku", methods=["POST", "GET"])
@app.route("/ssudoku", methods=["POST", "GET"])
@app.route("/csudoku", methods=["POST", "GET"])
def redirectToss():
    return redirect("/ss")


@app.route("/ss", methods=["POST", "GET"])
@login_required
def solveSudoku():
    # Assuming your compiled C file is named 'compiled_c_file'
    # c_file_path = 'path/to/compiled_c_file'
    # if request.method == "POST":
    #     return render
    if request.method == "GET":
        # unsolvedSudoko = request.args.get("sudoku")
        # if unsolvedSudoko:
        #     return redirect("/ss?s="+unsolvedSudoko)
        # if(unso)
        # c_file_path = "c_files/ss"
        # result = run_in_ter("./"+c_file_path+" 090600800000503400807000610000050007000790100000006300070000020040000000203061784" )
        # print(result)
        # result = result.stdout.decode()
        result = ""
        return render_template("solve_sudoku.html", result=result, comm="solve_sudoku")
    # return render_template("solveSudoku.html",result=result )



@app.route("/history_ss_api", methods=["POST", "GET"])
def history_ss_api():
    res = db.execute(
        "select  problem_str,solved_str,date_time,complexity_in_backtrack from history_for_ss where user_id = ? order by id desc limit 500;",
        session["user_id"],
    )
    if not res == []:
        i =0

        for k in range(len(res)):
            res[i] =  [j for j in res[i].values()]

            i+=1
        i =0
    # print(res[1].values())  # in case of empty its []
    # return render_template("history_ss.html", result=res, comm="solve_sudoku")
    return jsonify({"massage": res})
@app.route("/history_ss", methods=["POST", "GET"])
def history_ss():
    res = db.execute(
        "select  problem_str,solved_str,date_time,complexity_in_backtrack from history_for_ss where user_id = ? order by id desc limit 500;",
        session["user_id"],
    )
    if not res == []:
        i =0

        for k in range(len(res)):
            res[i] =  [j for j in res[i].values()]

            i+=1
        i =0
    # print(res[1].values())  # in case of empty its []
    return render_template("history_ss.html", result='', comm="history_ss")
    return jsonify({"massage": res})


# <<-------------------------------------------end application zone----------------------------------------------------->>


# . -----------------------------------------------------------------------------------------------------------------
# . ------------------------------------------------appZone end------------------------------------------------------
# . -----------------------------------------------------------------------------------------------------------------
@app.route("/hello.html/<name>")
@app.route("/hello.c/<name>")
@app.route("/hello/<name>")
@app.route("/hello<name>")
def hello(name):
    return f"Hello, {escape(name)}!"


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("secret"):
            return apology("must provide secret", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM ss_users WHERE username = ?",
            request.form.get("username"),
        )

        # Ensure username exists and secret is correct
        # if len(rows) != 1 or not check_secret_hash(
        #     rows[0]["hash"], request.form.get("secret")
        # ):
        if len(rows) != 1 or not rows[0]["secret"] == request.form.get("secret"):
            return apology("invalid username and/or secret", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("secret"):
            return apology("must provide secret", 400)
        elif request.form.get("secret") != request.form.get("confirmation"):
            return apology("must provide same confirmation secret", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM ss_users WHERE username = ?",
            request.form.get("username"),
        )

        # Ensure username exists and secret is correct
        if len(rows) > 0:
            return apology("Username already exists", 400)

        user_id = db.execute(
            # "INSERT INTO ss_users (username,hash, cash) VALUES (?,?,?)", request.form.get("username"),generate_secret_hash(request.form.get("secret")),10000,
            "INSERT INTO ss_users (username,secret) VALUES (?,?)",
            request.form.get("username"),
            request.form.get("secret"),
        )
        # print(rows)

        # Remember which user has logged in
        # session["user_id"] = rows[0]["id"]
        session["user_id"] = user_id

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")
    return render_template("register.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


# <<-------------------------------------------helper functions--------------------------------------------------------->>

import random
import string


def isStrOnlyContainDigits(str):
    pattern = r"\D+"
    return False if re.search(pattern, str) else True


def get_random_string(length):
    # choose from all lowercase letter
    # letters = string.ascii_lowercase
    # letters = string.printable
    letters = string.ascii_letters + string.digits
    result_str = "".join(random.choice(letters) for i in range(length))
    # print("Random string of length", length, "is:", result_str)
    return result_str


# def run_in_ter(arg1 , list_items = []):
def run_in_ter(cl=""):
    if cl == "":
        return "No args in cli"
    try:
        # Use subprocess to run the compiled C file
        # result = subprocess.check_output(
        #     [arg1, list_items], stderr=subprocess.STDOUT, text=True
        # )
        cl = cl.split(" ")
        result = subprocess.run(
            cl, capture_output=True, check=True
        )  # using decode() methode
        # [c_file_path, list_items],text=True, capture_output=True)
        # print(result)
        return [0, result]
    except subprocess.CalledProcessError as e:
        # Handle errors if the C file execution fails
        return [1, e.output]


# <<------------------------------------------end helper functions---------------------------------------------------------->>
