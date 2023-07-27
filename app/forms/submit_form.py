from flask_wtf import FlaskForm
from wtforms import StringField

class SubmitForm(FlaskForm):
  search = StringField('search')
