#Api to save or delete users

import sys
import base64
import re

def validate_password(password):
    if re.match(r'(?=^.{10,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*\d)', password) is None:
        print('password doesn\'t match requirements')
    else:
        return True
	
def validate_login(login):
    return True

def add_user (args):
    decoded_password = str(base64.b64decode(args [3]), 'utf-8')
    if validate_password(decoded_password) and validate_login(args[2]):
        info = 'ADD "' + args[1] + '", "' + args[2] + '", "' + decoded_password + '"'
        return info
    else:
        sys.exit(1)


def disable_user (args):
    info = 'DISABLE "' + args[1] +'"'
    return info;
	

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: --add <name> <login> <password> or --del <login>')
        sys.exit(1)

    if args[0] == '--add':
        info = add_user(args)

    if args[0] == '--del':
        info = disable_user(args)

    with open('data.txt', 'a') as file:
        file.write(info + '\n')


if __name__ == '__main__':
    main()
