from app import app
from flask import jsonify, request

@app.route('/get_neighbours/login/<string:login>')
def recommend_neighbours_by_login(login):
    return (jsonify(get_neighbours_by_login(login)))



def get_neighbours_by_login(login):
    return {1:'1', 2:'2'}