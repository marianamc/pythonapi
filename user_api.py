#API to save or delete users

import sys
import base64
import re

def validate_password(password):
    if re.match(r'(?=^.{10,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)', password) is None:
        print('password doesn\'t match the requirements')
        return False
    else:
        return True
	
def validate_login(login):
    with open('data.txt') as file:
        for entry in file:
            if entry.startswith("ADD") and entry.split(',')[1] == ' "' + login + '"':
                print(login + ' already exists')
                return False
    return True

def add_user (args):
    decoded_password = str(base64.b64decode(args [2]), 'utf-8')
    if validate_password(decoded_password) and validate_login(args[1]):
        info = 'ADD "' + args[0] + '", "' + args[1] + '", "' + decoded_password + '"'
        return info
    else:
        sys.exit(1)


def disable_user (args):
    info = 'DISABLE "' + args[0] +'"'
    return info;
	

def main():
    args = sys.argv[1:]

    if len(args) == 1:
        info = disable_user(args)
    elif len(args) == 3:
        info = add_user(args)
    else:
        print('Usage:\n To add new user: python user_api.py <name> <login> <password>\n To disable user: python user_api.py <login>')
        sys.exit(1)

    with open('data.txt', 'a') as file:
        file.write(info + '\n')


if __name__ == '__main__':
    main()
