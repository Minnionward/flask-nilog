from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

# Dummy user credentials
USER_CREDENTIALS = {'minion': '123QWEr'}

# Function to check if the username and password are valid
def check_credentials(username, password):
    return username in USER_CREDENTIALS and USER_CREDENTIALS[username] == password

# Home page with login form
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if check_credentials(username, password):
            return redirect(url_for('success'))
        else:
            return render_template('login.html', message='Invalid username or password')
    return render_template('login.html', message=None)

# Success page after successful login
@app.route('/success')
def success():
    return 'Login successful!'

if __name__ == '__main__':
    app.run(debug=True)
