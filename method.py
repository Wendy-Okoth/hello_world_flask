from flask import Flask, request, redirect, url_for # Import redirect and url_for

app = Flask(__name__)

@app.route('/login', methods=['POST', 'GET']) # Changed to /login
def function():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('welcome', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('welcome', name=user))

# You also need a 'welcome' route for the redirects to work
@app.route('/welcome/<name>')
def welcome(name):
    return f"Welcome {name}!"

if __name__ == '__main__':
    app.run(debug=True)