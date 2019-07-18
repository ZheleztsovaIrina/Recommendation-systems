@app.route('/get_neighbours/login/<string:login>')
def recommend_neighbours_by_login(login):
    return (jsonify(get_neighbours_by_login(login)))