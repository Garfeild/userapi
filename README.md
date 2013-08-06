# User API Example Project

User API is a basic demonstration of an API that accepts user registrations
and returns user list views and user detail views.

## Installation

User API requires the following packages:

- python3.3
- virtualenv-3.3
- pip

First, clone the Github project:

    git clone git@github.com:bwind/userapi.git

Then, cd into your project directory, create a virtualenv and install the
requirements:

    virtualenv-3.3 env
    . ./env/bin/activate
    pip install -r requirements.txt

To run User API as a development server, cd into the `src` directory and issue
the following command:

    python manage.py runserver

Create the necessary database tables:

    python manage.py syncdb

Answer 'no' when asked to create a superuser.

## API endpoints

### New user

User API features a list view that accepts new user registrations. An example
curl call follows:

    curl localhost:8000/users -X POST -d 'username=bar&password=foo' -v

A 409 will be returned in case the user already exists. On success, User API
will respond with a 201 status code and the newly generated user ID.

### Retrieve list of users

To retrieve a list of users, we need to provide Basic Authentication. In the
Python 3 shell:

    import base64; base64.b64encode(b'bar:foo')

Then, invoke curl as follows:

    curl localhost:8000/users -v -H "Authorization: Basic YmFyOmZvbw=="

### Retrieve user detail view

Requires Basic Authentication. Invoke curl as follows:

    curl localhost:8000/users/1 -v -H "Authorization: Basic YmFyOmZvbw=="
