from flask import Flask, flash, redirect, render_template, request, session
import sqlite3

app = Flask(__name__)
app.debug = True
app.config['TEMPLATES_AUTO_RELOAD'] = True


def connect_db():
    con = sqlite3.connect("todo.db")
    return con

@app.route("/")
def index():
    con = connect_db()
    cur = con.cursor()
    cur.execute("SELECT * FROM todos;")
    todos = cur.fetchall()
    con.commit()
    con.close()
    return render_template("index.html", todos = todos)


@app.route("/add", methods = ["POST"])
def add():

    title = request.form.get("title")
    desc = request.form.get("desc")

    print(f"Title: {title}, Description: {desc}")
    con = connect_db()
    cur = con.cursor()
    cur.execute("INSERT INTO todos (title, desc) VALUES (?, ?);", (title, desc))
    con.commit()
    con.close()
    return redirect("/")