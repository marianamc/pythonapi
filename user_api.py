#Api to save or delete users

import sys

def main():
    args = sys.argv[1:]

    if not args:
        print('usage: --add name login password or --del login')
        sys.exit(1)

    if args[0] == '--add':
        info = 'ADD "' + args[1] + '", "' + args[2] + '", "' + args [3] + '"'

    if args[0] == '--del':
        info = 'DISABLE "' + args[1] +'"'

    with open('data.txt', 'a') as file:
        file.write(info + '\n')


if __name__ == '__main__':
    main()
