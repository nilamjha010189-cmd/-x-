import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    try:
        return render_template('index.html')
    except:
        return "<h1>Renox Web Bot Host is Running Successfully!</h1>"

@app.route('/login')
def login():
    try:
        return render_template('login.html')
    except:
        return "Login page coming soon."

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)