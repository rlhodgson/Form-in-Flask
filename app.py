# https://www.tutorialspoint.com/flask/flask_sqlite.htm
# http://flask.pocoo.org/docs/0.12/patterns/sqlite3/
# https://github.com/stevedunford/NZVintageRadios
import mysql.connector
from flask import Flask, Response, render_template, abort

# Creates a Flask object called 'app' that we can use throughout the programme
app = Flask(__name__)

# This is the function that controls the main page of the web site
@app.route("/")
def index():
  return render_template('main.html',
                          title="Check the Track")

# This is the function shows the Athletes page
@app.route("/athletes")
def athletes():
  import sqlite3
  conn = sqlite3.connect('tracks.db')
  cursor = conn.cursor()
  results = cursor.execute("SELECT * from Tracks")
  medalists = [dict(trackid=row[0], trackname=row[1], difficulty=row[2], conditions=row[3], date=row[4]) for row in results]

  return render_template('athletes.html',title="Track Details",medalists=medalists)

@app.route('/form', methods=['GET', 'POST'])
def login():
  
  return render_template('form.html', title="Login")  

# This function deals with any missing pages and shows the Error page
@app.errorhandler(404)
def page_not_found(e):
  return render_template('404.html', title="404"), 404

if __name__ == "__main__":
    app.run(debug=True)