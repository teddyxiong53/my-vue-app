from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3
from config import Config
app = Flask(__name__)
CORS(app)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/register', methods=['POST'])
def register():
    conn = get_db_connection()
    cursor = conn.cursor()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    try:
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        result = {'message': 'User registered successfully'}
    except sqlite3.IntegrityError:
        result = {'error': 'Username already exists'}
    finally:
        conn.close()

    return jsonify(result)

@app.route('/login', methods=['POST'])
def login():
    conn = get_db_connection()
    cursor = conn.cursor()
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
    user = cursor.fetchone()
    conn.close()

    if user:
        result = {'message': 'Login successful'}
    else:
        result = {'error': 'Invalid username or password'}

    return jsonify(result)

@app.route('/')
def home():
    return jsonify(message="Hello, World!")

if __name__ == '__main__':
    app.run(host=Config.HOST, debug=True, port=Config.PORT)
