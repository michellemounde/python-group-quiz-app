from flask import Flask, render_template
from flask_migrate import Migrate
from .config import Config
from app.api.home import home

app = Flask(__name__)

app.config.from_object(Config)
app.register_blueprint(home, url_prefix='/home')

@app.errorhandler(404)
def not_found(err):
    return render_template('404.html')
