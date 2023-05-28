from flask import Flask, render_template, request, redirect, url_for, jsonify
import json
from scripts.houses import get_houses_address, update_house

app = Flask(__name__)


@app.route('/api/houses/list', methods=['GET'])
def get_list_houses():
    if request.method == 'GET':
        return get_houses_address()
    else:
        return 'BAD REQUEST'
    

@app.route('/api/houses/update', methods=['POST'])
def api_add_house():
    if request.method == 'POST':
        print(request.form)    
        return jsonify(update_house(json.loads(request.form["info"]), request.files['video']))
    else:
        return 'BAD REQUEST'



@app.route('/')
@app.route('/search', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run('0.0.0.0', 5050)