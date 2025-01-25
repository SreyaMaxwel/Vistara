from flask import Flask, request, jsonify, render_template, redirect

app = Flask(__name__)

# Dictionary to store user credentials
users = {}

@app.route('/')
def home():
    return render_template('template.html')  # The provided HTML file should be saved as 'templates/index.html'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Validate user credentials
        if username in users and users[username] == password:
            return jsonify({"message": "Login successful!", "status": "success"})
        elif username not in users:
            return jsonify({"message": "Username not found. Please register.", "status": "error"})
        else:
            return jsonify({"message": "Incorrect password. Please try again.", "status": "error"})
    return render_template('login.html')  # Render login page

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Register new user
        if username in users:
            return jsonify({"message": "Username already exists. Choose a different username.", "status": "error"})
        else:
            users[username] = password
            return jsonify({"message": "Registration successful!", "status": "success"})
    return render_template('register.html')  # Render register page

if __name__ == '__main__':
    app.run(debug=True)
