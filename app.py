from flask import Flask, request, jsonify
from models import connect_db
from helper import is_valid_email, is_valid_mobile, assistant_exists

app = Flask(__name__)

# create a new assistant
@app.route('/assistant', methods=['POST'])
def create_assistant():
    conn = connect_db()
    cursor = conn.cursor()
    data = request.get_json()
    
    # Check if a user with the same email or mobile already exists
    cursor.execute("SELECT * FROM assistants WHERE email = ? OR mobile = ?", (data['email'], data['mobile']))
    existing_user = cursor.fetchone()
    if existing_user:
        conn.close()
        return jsonify({'error': 'User already exists with the same email or mobile number'}), 400

    # Validate email format
    if not is_valid_email(data['email']):
        conn.close()
        return jsonify({'error': 'Invalid email format'}), 400
    
    # Validate mobile number format
    if not is_valid_mobile(data['mobile']):
        conn.close()
        return jsonify({'error': 'Mobile number must be 10 digits long'}), 400
    
    # If no existing user found, then create a new assistant
    cursor.execute("INSERT INTO assistants (name, mobile, email, salary, city, country, department, role) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                   (data['name'], data['mobile'], data['email'], data['salary'], data['city'], data['country'], data['department'], data['role']))
    assistant_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return jsonify({'assistant_id': assistant_id}), 201

# Get details of all assistants
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
    
    if not assistant_exists(conn, assistant_id):
        conn.close()
        return jsonify({'error': 'Assistant with the specified ID does not exist'}), 404
    
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
    
    if not assistant_exists(conn, assistant_id):
        conn.close()
        return jsonify({'error': 'Assistant with the specified ID does not exist'}), 404
    
    cursor.execute("DELETE FROM assistants WHERE id=?", (assistant_id,))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Assistant deleted successfully'}), 200

if __name__ == '__main__':
    app.run(debug=True)