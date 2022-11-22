# django-chat-api
A chat api built with the django framework

## Virtual environment
This project uses the venv virtual enironment which can be installed by running the command ```python -m venv name_of_environment```.
Once it's installed, run ```name_of_environment\Scripts\activate``` to activate the environment and ```name_of_environment\Scripts\deactivate``` to deactivate it.

## Django Rest Framework
This project uses the Django Rest Framework to create Apis

## Running the server
To run Django server, write the following command ```python manage.py runserver```

## Auth Token
When testing in postman, use ```Authorization     Token token``` in the headers of postman after signing in to access protected routes.

## Routes
Below are the routes for the project

General:
/accounts/login/
/accounts/signup/

Protected:
/chat/message/
/chat/message/
/chat/message?receiver__username=userId(For filtered search)
