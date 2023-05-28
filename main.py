from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from scripts.houses import get_houses_address, update_house, add_house, delete_house, delete_house_room

app = Flask(__name__)

@app.route('/api/houses/list', methods=['GET'])
def get_list_houses():
    if request.method == 'GET':
        return get_houses_address()
    else:
        return jsonify({'success': False})    

@app.route('/api/houses/add', methods=['POST'])
def add_address():
    if request.method == 'POST':
        add_house(request.form)
        return redirect(url_for('index'))
    else:
        return jsonify({'success': False})

@app.route('/api/houses/delete', methods=['POST'])
def delete_address():
    if request.method == 'POST':
        if delete_house(request.form['address']) == True:
            return redirect(url_for('index'))
        else:
            return jsonify({'success': False})
    else:
        return jsonify({'success': False})
    
@app.route('/api/houses/delete/room', methods=['POST'])
def delete_house_r():
    if request.method == 'POST':
        if delete_house_room(request.json['address'], request.json['floor'], request.json['flat'], request.json['room_type']) == True:
            return jsonify({'success': True})
        else:
            return jsonify({'success': False})
    else:
        return jsonify({'success': False})

@app.route('/api/houses/update', methods=['POST'])
def api_add_house():
    if request.method == 'POST':  
        return update_house(json.loads(request.form["info"]), request.files['video'])
    else:
        return jsonify({'success': False})

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html', houses = get_houses_address())

if __name__ == "__main__":
    app.run('0.0.0.0', 5050)