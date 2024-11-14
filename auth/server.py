import jwt,datetime,os
from flask import Flask,request
from flask_mysqldb import MySQL

server = Flask(__name__)
mysql = MySQL(server)      

#config

server.config["MYSQL_HOST"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_USER"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_PASSWORD"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_DB"] = os.environ.get("MYSQL_HOST")
server.config["MYSQL_PORT"] = os.environ.get("MYSQL_HOST")

@server.route("/login",methods = ["POST"])
def login():
    auth = request.authorization
    if not auth:
        return "missing cred",401
    # check db for username and passowrd
    

