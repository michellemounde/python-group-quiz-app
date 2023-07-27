# How to Setup project for Flask Backend with Jinja Templates

## Installations
As per requirements.txt - Not sure if we need, werkzeug comes with flask
Do we need auth? flask-login
Do we need a database? sqlalchemy, flask-sqlalchemy, alembic, flask-migrate

## Structure
A. app
  1. api
  2. forms
  3. templates
  Auto-generated
  4. models
  5. seeds
  6. migrations
B. .flaskenv
C. .env
D. requirements.txt - when run generates Pipfile & Pipfile.lock

## Remember
pipenv
.flaskenv
.env
setup imports through __init__.py's

## Setup
0. create .env(with SECRET KEY & SQLALCHEMY keys) and .flaskenv
1. pipenv install -r requirements.txt
2. setup config
3. create app __init__.py: instatiate Flask, config & register blueprints if present
4. create blueprints in api
5. create forms with flask_wtf and wtforms
6. create templates
7. database creation with sqlalchemy & flask_sqlalchemy
8. database migrations with alembic and flask_migrate
