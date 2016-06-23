# FlaskProject
[Flask][fl] app using modular blueprints.

The structure is a combination of [Large app how to][la] and [overholt][oh].

Features:

- [Flask-Security][fs]
- [Jinja2][jj] template engine
- Twitter Bootstrap

This webapp requires these programs: 

- Python 2.7.*
- pip
- Virtualenv
- Bower

#### 1. Activate virtualenv

	$ virtualenv env
	$ source env/bin/activate

#### 2. Install all required Python libraries

	$ pip install -r requirements.txt

#### 3. Install all required JS libraries

	$ cd /flaskproject/static
	$ bower install

#### 4. Initialize database

	$ python seed.py

#### 5. Run the Flask project

	$ python run.py

[fl]: http://flask.pocoo.org/
[fs]: https://github.com/mattupstate/flask-security
[jj]: http://jinja.pocoo.org/
[oh]: https://github.com/mattupstate/overholt
[la]: https://github.com/pallets/flask/wiki/Large-app-how-to
