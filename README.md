# FlaskProject
[Flask](http://flask.pocoo.org/) app using modular blueprints.

The structure is a combination of [Large app how to](https://github.com/pallets/flask/wiki/Large-app-how-to) and [overholt](https://github.com/mattupstate/overholt).

Features:

- [Flask-Security](https://github.com/mattupstate/flask-security)
- [Jinja2](http://jinja.pocoo.org/) template engine
- Twitter Bootstrap

This web app requires these programs: 

- Python 3.9.16
- pip
- python3.10-venv

#### 1. First time environment initialization

	$ python3 -m venv venv
	$ source venv/bin/activate

#### 2. Activate environment

	$ source venv/bin/activate

#### 3. Install all required Python libraries

	$ pip install -r requirements.txt

#### 4. Initialize database

	$ python seed.py

#### 5. Run the Flask project

	$ python run.py

[fl]: http://flask.pocoo.org/
[fs]: https://github.com/mattupstate/flask-security
[jj]: http://jinja.pocoo.org/
[oh]: https://github.com/mattupstate/overholt
[la]: https://github.com/pallets/flask/wiki/Large-app-how-to
