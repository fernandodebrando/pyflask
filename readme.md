
**Test create project with flask and deploying with Setuptools**

    mkdir pyflask
    cd pyflask
    sudo apt-get install python3-venv
    python3 -m venv venv
    . venv/bin/activate
    export FLASK_APP=pyflask
    export FLASK_ENV=development
    pip install -e . 
    flask run

**Test API**
    $ pip install requests
    $ python
    >>> import requests
    >>> r = requests.get('http://localhost:5000/product/')
    >>> r.json()
    {}
    >>> r = requests.post('http://localhost:5000/product/', data={'name': 'iPhone 6s', 'price': 699})
    >>> r.json()
    {u'1': {u'price': u'699.0000000000', u'name': u'iPhone 6s'}}
    >>> r = requests.post('http://localhost:5000/product/', data={'name': 'iPad Pro', 'price': 999})
    >>> r.json()
    {u'2': {u'price': u'999.0000000000', u'name': u'iPad Pro'}}
    >>> r = requests.get('http://localhost:5000/product/')
    >>> r.json()
    {u'1': {u'price': u'699.0000000000', u'name': u'iPhone 6s'}, u'2': {u'price': u'999.0000000000', u'name': u'iPad Pro'}}
    >>> r = requests.get('http://localhost:5000/product/1')
    >>> r.json()
    {u'price': u'699.0000000000', u'name': u'iPhone 6s'}

**Patterns for Flask**
- http://flask.pocoo.org/docs/1.0/patterns/

**Deploying with Setuptools**
- http://flask.pocoo.org/docs/1.0/patterns/distribute/

**Deploying with Fabric**
- http://flask.pocoo.org/docs/1.0/patterns/fabric/

**SQLAlchemy in Flask**
- http://flask-sqlalchemy.pocoo.org/2.3/
