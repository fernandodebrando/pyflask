Test create project with flask and deploying with Setuptools
mkdir pyflask
cd pyflask
sudo apt-get install python3-venv
python3 -m venv venv
. venv/bin/activate
export FLASK_APP=pyflask
export FLASK_ENV=development
pip install -e . 
flask run

Patterns for Flask
http://flask.pocoo.org/docs/1.0/patterns/

Deploying with Setuptools
http://flask.pocoo.org/docs/1.0/patterns/distribute/

Deploying with Fabric
http://flask.pocoo.org/docs/1.0/patterns/fabric/

SQLAlchemy in Flask
http://flask-sqlalchemy.pocoo.org/2.3/