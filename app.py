from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)

# establish connection with SQLite database
def connect_db():
    conn = sqlite3.connect('assistants.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS assistants (
                          id INTEGER PRIMARY KEY AUTOINCREMENT,
                          name TEXT,
                          mobile TEXT,
                          email TEXT,
                          salary REAL,
                          city TEXT,
                          country TEXT,
                          department TEXT,
                          role TEXT
                      )''')
    conn.commit()
    return conn

# create a new assistant
@app.route('/assistant', methods=['POST'])
def create_assistant():
    conn = connect_db()
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("INSERT INTO assistants (name, mobile, email, salary, city, country, department, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (data['name'], data['mobile'], data['email'], data['salary'], data['city'], data['country'], data['department'], data['role']))
    assistant_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'assistant_id': assistant_id}), 201

# Get details of all assistant
@app.route('/assistants', methods=['GET'])
def get_all_assistants():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assistants")
    assistants = cursor.fetchall()
    conn.close()
    if assistants:
        return jsonify([dict(assistant) for assistant in assistants]), 200
    else:
        return jsonify({'error': 'No assistants found'}), 404

# Get details of a specific assistant
@app.route('/assistant/<int:assistant_id>', methods=['GET'])
def get_assistant(assistant_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assistants WHERE id = ?", (assistant_id,))
    assistant = cursor.fetchone()
    conn.close()
    if assistant:
        return jsonify(dict(assistant)), 200
    else:
        return jsonify({'error': 'Assistant not found'}), 404

# Update details of a specific assistant
@app.route('/assistant/<int:assistant_id>', methods=['PUT'])
def update_assistant(assistant_id):
    conn = connect_db()
    cursor = conn.cursor()
    data = request.get_json()
    cursor.execute("UPDATE assistants SET name=?, mobile=?, email=?, salary=?, city=?, country=?, department=?, role=? WHERE id=?",
                   (data['name'], data['mobile'], data['email'], data['salary'], data['city'], data['country'], data['department'], data['role'], assistant_id))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Assistant updated successfully'}), 200

# Delete a specific assistant
@app.route('/assistant/<int:assistant_id>', methods=['DELETE'])
def delete_assistant(assistant_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM assistants WHERE id=?", (assistant_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Assistant deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)
