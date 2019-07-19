from app import app
from flask import jsonify, request
from GIT import *

# http://10.1.1.1:5000/login?username=alex&password=pw1


@app.route('/by_login', methods=['GET'])
def by_login():
    username = request.args.get('username')
    print(username)
    password= request.args.get('password')
    print(password)
    login_git(username,password)



# def get_neighbours_by_login(login):
#     return {1:'1', 2:'2'}