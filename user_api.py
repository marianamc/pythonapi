#Api to save or delete users

import sys
import base64

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: --add name login password or --del login')
        sys.exit(1)

    if args[0] == '--add':
        info = 'ADD "' + args[1] + '", "' + args[2] + '", "' + str(base64.b64decode(args [3]), 'utf-8') + '"'

    if args[0] == '--del':
        info = 'DISABLE "' + args[1] +'"'

    with open('data.txt', 'a') as file:
        file.write(info + '\n')


if __name__ == '__main__':
    main()
