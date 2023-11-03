from flask import Flask, request, session, redirect, url_for, render_template

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace 'your_secret_key' with a secret key of your choice.

@app.route('/')
def home():
    # Check if the user is already logged in by looking for their username in the session.
    if 'username' in session:
        username = session['username']
        return f'Hello, {username}! <a href="/logout">Logout</a>'
    else:
        return 'Welcome! <a href="/login">Login</a>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # When the user submits a login form, store their username in the session.
        session['username'] = request.form['username']
        return redirect(url_for('home'))
    return render_template('login.html')  # Create a login form in a template.

@app.route('/logout')
def logout():
    # Remove the user's username from the session to log them out.
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(port=5002, debug=True)
