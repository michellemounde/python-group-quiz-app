from flask import Blueprint, render_template, request
from app.forms import SubmitForm

home = Blueprint('home', __name__)

@home.route('/')
def show_submit():
  form = SubmitForm()
  return render_template('home.html', form=form)

@home.route('/', methods=['POST'])
def submit():
  form = SubmitForm()

  if form.validate_on_submit():
    print(form.data)
  return render_template('home.html', form=form)
