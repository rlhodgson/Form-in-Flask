from flask_wtf import FlaskForm
from wtforms import IntegerField, TextField, TextAreaField, SelectField, BooleanField, RadioField
from wtforms.validators import DataRequired, Optional, ValidationError
import models


class Add_Track(FlaskForm):
  
  #trackname = TextField('Trackname', validators=[DataRequired()])
  trackname = SelectField(u'Name of Track', choices=[('Milford', 'Milford'), ('Routeburn', 'Routeburn'), ('Heaphy', 'Heaphy')])
  #difficulty = IntegerField('Difficulty', validators=[Optional()])
  difficulty = SelectField(u'Difficulty', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10','10')])
  #conditions = TextAreaField('Conditions')
  date = TextAreaField('Date') 
  conditions = RadioField('Conditions', choices = [('Muddy Track', 'Muddy Track'),('Fallen Trees','Fallen Trees'), ('Landslides', 'Landslides'),('Flooding','Flooding'), ('Loose Gravel', 'Loose Gravel'),('Rutted Track','Rutted Track')])