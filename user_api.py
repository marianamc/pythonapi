#API to save or delete users
from flask import Flask
import sys
import base64
import re

app = Flask(__name__)

def validate_password(password):
    if re.match(r'(?=^.{10,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)', password) is None:
        return False
    return True
	
def validate_login(login):
    with open('data.txt') as file:
        for entry in file:
            if entry.startswith("ADD") and entry.split(',')[1] == ' "' + login + '"':
                return False
    return True

def add_user (name, login, password):
    info = 'ADD "' + name + '", "' + login + '", "' + password + '"'
    return info

def disable_user (login):
    info = 'DISABLE "' + login +'"'
    return info;
	

@app.route('/disable/<login>', methods=['GET'])
def disable_login(login):
    info = disable_user(login)
	
    with open('data.txt', 'a') as file:
        file.write(info + '\n')
    return info

@app.route('/add/<name>/<login>/<password>', methods=['GET'])
def add_login(name, login, password):
    decoded_password = str(base64.b64decode(password), 'utf-8')
	
    if validate_password(decoded_password) == False:
        return 'Password doesn\'t match the requirements'
    elif validate_login(login) == False:
        return 'User ' + login + ' already exists'
    else:
        info = add_user(name, login, decoded_password)
    
        with open('data.txt', 'a') as file:
            file.write(info + '\n')
        return info

if __name__ == '__main__':
    app.run()
