from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/api/status')
def status():
    return jsonify({
        'status': 'online',
        'message': 'Personal Finance Tracker Flask backend connected'
    })

# Serve static files (CSS, JS, images)
@app.route('/<path:path>')
def static_proxy(path):
    if os.path.exists(path):
        return send_from_directory('.', path)
    return jsonify({'error':'not found'}), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
