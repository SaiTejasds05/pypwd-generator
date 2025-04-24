from flask import Flask, render_template, jsonify, request
import random
import string
import logging

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)

def generate_password(length=12, use_uppercase=True, use_numbers=True, use_special_chars=True):
    # Define character sets
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase if use_uppercase else ''
    number_chars = string.digits if use_numbers else ''
    special_chars = '!@#$%^&*()_+-=[]{}|;:,.<>?' if use_special_chars else ''
    
    # Combine all allowed characters
    all_chars = lowercase_chars + uppercase_chars + number_chars + special_chars
    
    # Ensure at least one character from each selected type
    password = []
    if use_uppercase:
        password.append(random.choice(uppercase_chars))
    if use_numbers:
        password.append(random.choice(number_chars))
    if use_special_chars:
        password.append(random.choice(special_chars))
    password.append(random.choice(lowercase_chars))  # Always include lowercase
    
    # Fill the rest of the password length
    remaining_length = length - len(password)
    password.extend(random.choice(all_chars) for _ in range(remaining_length))
    
    # Shuffle the password characters
    random.shuffle(password)
    
    # Join and return the password
    return ''.join(password)

@app.route('/')
def index():
    app.logger.info('Homepage accessed')
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    app.logger.info('Password generation requested')
    data = request.get_json()
    length = max(int(data.get('length', 12)), 8)
    use_uppercase = data.get('uppercase', True)
    use_numbers = data.get('numbers', True)
    use_special_chars = data.get('special', True)
    
    password = generate_password(
        length=length,
        use_uppercase=use_uppercase,
        use_numbers=use_numbers,
        use_special_chars=use_special_chars
    )
    
    return jsonify({'password': password})

if __name__ == '__main__':
    # Enable debug mode and bind to all interfaces
    app.logger.info('Starting server...')
    app.run(
        debug=True,
        host='0.0.0.0',  # Bind to all interfaces
        port=5000,
        use_reloader=True
    ) 