import re

# Function to validate email format
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(email_regex, email)

# Function to validate mobile number format
def is_valid_mobile(mobile):
    return len(mobile) == 10 and mobile.isdigit()

# Function to check if the assistant with the specified ID exists or not
def assistant_exists(conn, assistant_id):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM assistants WHERE id = ?", (assistant_id,))
    existing_assistant = cursor.fetchone()
    return existing_assistant is not None
