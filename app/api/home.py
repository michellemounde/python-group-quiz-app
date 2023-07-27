from flask import Blueprint, render_template, request
from app.forms import SubmitForm

home = Blueprint('home', __name__)

@home.route('/')
def show_submit():
  return render_template('home.html')

@home.route('/', methods=['POST'])
def submit():
  form = SubmitForm()

  if form.validate_on_submit():
    print('Request')
    print(request)
    print(form.search.data)

@home.route('/delete', methods=['DELETE'])
