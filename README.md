# pythonapi

## user_api.py

user_api.py is an API that will handle requests to add or disable users and write the corresponding instructions into data.txt file.

## How-to run

python user_api.py path-to-data.txt

## Add an user

Add user: ./add/name/login/password

API will check for duplicated users on data.txt and will validate the password that must be provided in Base64, be at least 10 characters long with at least one uppercase, one lowercase and one digit.

## Disable an user

Disable User: ./disable/login
