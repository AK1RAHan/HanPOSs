from flask import Flask, render_template, request
import os
import sqlite3

app = Flask(__name__)

@app.route('/')
def homeO():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)