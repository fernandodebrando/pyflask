from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/pyflask.db'
db = SQLAlchemy(app)

from pyflask.api.views import api
app.register_blueprint(api)
 
db.create_all()

