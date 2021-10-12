National Communications Software Security Laboratory (NCSS Lab) Website
------
National Communications Software Security Laboratory web system.  
This project is developed by [Django][1].  


### Installation
Clone project via [git][2].  
```sh
$ git clone [GIT-PATH] NCSSLAB
```

Then install all requirements.  
Uncomment gunicorn requirements if we want to run system with **gunicorn**.  
```python
...
# For gunicorn: Uncomment here
-r requirements-gunicorn.txt
```

Install requirements via [pip][3].  
```sh
$ pip install -r requirements.txt
```

Install requirements for development.  
```sh
$ pip install -r requirements-dev.txt
```


### How to use

#### Setup Project Configuration
This project allows us to configure Django application with environment variables.  

##### ✦ Option 1: Use *.env* file

Copy **.env** from **.env.example**.  
```sh
$ cp .env.example .env
```

Edit **.env file**.  
```sh
# Enable or disable debug mode.
DEBUG=False

SECRET_KEY=[YOUR_SECRET_KEY]

# A list of strings representing the host/domain names that this Django site can serve.
#   Example: ALLOWED_HOSTS=HOST_A,HOST_B,HOST_C
#   Example: ALLOWED_HOSTS=*
ALLOWED_HOSTS=[HOSTS_LIST]

# Database Configuration.
# See https://django-environ.readthedocs.io/en/latest/#supported-types
# Supported Types: db_url
#    PostgreSQL format:
#       postgres://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]
#    SQLite format:
#       sqlite:///[YOUR DATABASE PATH]
#
#    Example:
#       DATABASE_URL=postgres://postgres:password@localhost:5432/database
#       DATABASE_URL=sqlite:///db.sqlite3
DATABASE_URL=sqlite:///db.sqlite3

```

##### ✦ Option 2: Set environment variables directly

Set environment variables for django settings.  
```sh
#!/bin/bash

# Set DJANGO_READ_ENV_FILE to False to ignore .env file
# if you have already created it.
export DJANGO_READ_ENV_FILE=False

# Enable or disable debug mode.
export DEBUG=False

export SECRET_KEY=[YOUR_SECRET_KEY]

# A list of strings representing the host/domain names that this Django site can serve.
#   Example: ALLOWED_HOSTS=HOST_A,HOST_B,HOST_C
#   Example: ALLOWED_HOSTS=*
export ALLOWED_HOSTS=[HOSTS_LIST]

# Database Configuration.
# See https://django-environ.readthedocs.io/en/latest/#supported-types
# Supported Types: db_url
#    PostgreSQL format:
#       postgres://[USER]:[PASSWORD]@[HOST]:[PORT]/[DATABASE_NAME]
#    SQLite format:
#       sqlite:///[YOUR DATABASE PATH]
#
#    Example:
#       DATABASE_URL=postgres://postgres:password@localhost:5432/database
#       DATABASE_URL=sqlite:///db.sqlite3
export DATABASE_URL=sqlite:///db.sqlite3

```

#### Create Tables for Models in Your Database
Django prepared migration files to apply to the database.  
```sh
$ python manage.py migrate
```

#### Collect All Static Files
In production environment, it need to collect all static files into STATIC_ROOT directory  
```sh
$ python manage.py collectstatic
```

#### Start Application

##### Start application on a local development server
Use the following command to start application:  
Default URL is [http://127.0.0.1:8000/](http://127.0.0.1:8000/)  
```sh
$ python manage.py runserver
```

Or start application with specific IP address and port.  
```sh
$ python manage.py runserver [IP Address]:[Port]
```

##### Start application with Gunicorn 
Start application with gunicorn:  
Default URL is [http://127.0.0.1/](http://127.0.0.1/)  
```console
$ gunicorn -c python:gunicorn_conf NCSSLAB.wsgi
```

Edit gunicorn_conf.py start application to modify IP address and port.
```python
import multiprocessing

# Edit HERE!!!
bind = "0.0.0.0:80"
```


Stop gunicorn by following command.  
```console
$ pkill gunicorn
```


[1]:https://www.djangoproject.com/ "Django"
[2]:https://git-scm.com/ "git"
[3]:https://pip.pypa.io/en/stable/installing/ "pip"