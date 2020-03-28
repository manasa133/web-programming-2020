import os
from flask import Flask, session
from flask import render_template
from flask import request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import User
from datetime import datetime


app = Flask(__name__)

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db= scoped_session(sessionmaker(bind=engine))
Base = declarative_base()
Base.query = db.query_property()
Base.metadata.create_all(bind=engine)

@app.route("/")
def index():
	return "Project 1: TODO"

@app.route("/register",methods=['GET','POST'])
def register():
	if request.method == 'GET':
		return render_template("register.html")
	elif request.method == 'POST':
		uname = request.form['uname']
		passw = request.form['passw']
		time=datetime.now()
		# try:
		new = User(name=uname, passw=passw,time=time)
		db.add(new)
		db.commit()
		# except Exception as e:
		# 	print(str(e))
	return render_template("register.html")


@app.route("/admin",methods=['GET','POST'])
def admin():
	users = db.query(User)
	return render_template("admin.html",result = users)

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/auth",methods=['GET','POST'])
def auth():
	users = db.query(User)
	message = ["Login failed"]
	if request.method == 'POST':
		uname = request.form['uname']
		passw = request.form['passw']
		for user in users:
			if(user.name==uname):
				if(user.passw == passw):
					return render_template("home.html")
	print("Failed")
	return render_template("register.html",result=message)



