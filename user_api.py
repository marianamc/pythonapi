#API to save or delete users
from flask import Flask
import sys
import base64
import re

app = Flask(__name__)
path = ''

def validate_password(password):
    if re.match(r'(?=^.{10,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)', password) is None:
        return False
    return True
	
def validate_login(login):
    with open(path +'/data.txt') as file:
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

def write_file(info):
    with open(path +'/data.txt', 'a') as file:
        file.write(info + '\n')
    return	

@app.route('/disable/<login>', methods=['GET'])
def disable_login(login):
    info = disable_user(login)
    write_file(info)
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
        write_file(info)
        return info

if __name__ == '__main__':
    path  = sys.argv[1]
    app.run()
