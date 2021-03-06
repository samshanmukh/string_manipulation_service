# String Manipulation Service

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/samshanmukh/string_manipulation_service.git
$ cd string_manipulation_service
```

Create a virtual environment to install dependencies in and activate it:

```sh
$ python env app-service-env
$ source app-service-env/bin/activate
```

Then install the dependencies:

```sh
(env)$ pip install -r requirements.txt
```
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `python env`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd project
(env)$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

In order to test the purchase flows, fill in the account details in
`project/gc_app/views.py` to match your **SANDBOX** developer credentials.

## Walkthrough


```
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```

## To work with django model

```
(env)$ python3 manage.py shell
```
