from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

BACKEND_URL = os.getenv('BACKEND_URL', 'http://localhost:3000')

@app.route('/')
def home():
    return render_template('index.html', backend_url=BACKEND_URL)
    
@app.route('/api', methods=['GET'])
def api():
    response = requests.get(f'{BACKEND_URL}/api')
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
    