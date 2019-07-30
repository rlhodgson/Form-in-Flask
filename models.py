from forminflask import db

class Track(db.Model):
  __tablename__ = 'Tracks'
  
  trackname = db.Column(primary_key=True)
  difficulty = db.Column(db.Integer)
  conditions = db.Column(db.String(80))
  date = db.Column(db.String(80))
  
  def __repr__(self):
    return 'Track: {}'.format(self.trackname)
