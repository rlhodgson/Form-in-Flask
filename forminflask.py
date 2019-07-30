from flask import Flask, render_template, redirect, request, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import date
import sqlite3
from flask import Flask, Response, render_template, abort


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tracks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'correcthorsebatterystaple'
WTF_CSRF_ENABLED = True
WTF_CSRF_SECRET_KEY = 'sup3r_secr3t_passw3rd'
db = SQLAlchemy(app)

import models # need 'db' to import models
from forms import Add_Track 

# This is the function that controls the main page of the web site
@app.route("/")
def index():
  import sqlite3
  conn = sqlite3.connect('tracks.db')
  cursor = conn.cursor()
  results = cursor.execute("SELECT * from Tracks where TrackID < 36 ORDER BY TrackID DESC")
  tracks = [dict(trackid=row[0], trackname=row[1], difficulty=row[2], conditions=row[3], date=row[4], image=row[5]) for row in results]  
  
  return render_template('main.html',
                          title="Check the Track", tracks=tracks)

@app.route("/athletes")
def athletes():
  import sqlite3
  conn = sqlite3.connect('tracks.db')
  cursor = conn.cursor()
  results = cursor.execute("SELECT * from Tracks ORDER BY TrackID DESC")
  medalists = [dict(trackid=row[0], trackname=row[1], difficulty=row[2], conditions=row[3], date=row[4]) for row in results]

  return render_template('athletes.html',title="Track Details",medalists=medalists)
    

@app.route("/form", methods=['GET', 'POST'])
def add_info():
    form = Add_Track()
    if request.method=='GET':
        return render_template('form.html', form=form, title="Add track information")
    else:
        if form.validate_on_submit():
            new_track = models.Track()
            new_track.trackname = form.trackname.data
            new_track.difficulty = form.difficulty.data
            new_track.conditions = form.conditions.data
            today = date.today()
            dates = today.strftime("%m/%d/%y")            
            new_track.date = dates
            db.session.add(new_track)
            db.session.commit()
            return redirect(url_for('athletes'))
        else:
            return render_template('form.html', form=form, title="Add track information")


@app.route("/details")
def details():
    conn = sqlite3.connect('tracks.db')
    cursor = conn.cursor()
    results = cursor.execute("SELECT * from Tracks")
    medalists = [dict(trackid=row[0], trackname=row[1], difficulty=row[2], conditions=row[3], date=row[4]) for row in results]
    
    return render_template('track_deets.html',title="Track Details",medalists=medalists)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)