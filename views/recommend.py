from app import app
from flask import jsonify, request
from GIT import *

# http://192.168. . :5000/login?username=alex&password=pw1


@app.route('/login')
def login():
    username = request.args.get('username')
    password= request.args.get('password')
    return(jsonify(get_neighbours_by_login(username,password)))



def get_neighbours_by_login(username,password):
    return{1:login_git(username,password)[0],2:login_git(username,password)[1],3:login_git(username,password)[2],
           4:login_git(username,password)[3],5:login_git(username,password)[4]}