from os import listdir
from os.path import isdir
from os import chdir
from sys import argv

ignore_list = [
    'node_modules',
    '.git',
    '.DS_Store',
    'build',
    'dist',
    'out',
    '.idea',
    '.mvn',
    '.gitignore',
    '.dockerignore',
    '.npm'
    ]


def print_dtree(DEPTH, file_list, num):
    if num > DEPTH:
        return
    for file in file_list:
        if file in ignore_list:
            continue
        print('├' + '─'*num + ' ' + str(file))
        if(isdir(file)):
            chdir(file)
            new_file_list = listdir()
            new_file_list.sort()
            print_dtree(DEPTH, new_file_list, num+1)
            chdir('../')


def main():
    try:
        folder_path = argv[1]
        chdir(folder_path)
    except IndexError:
        print('No path found')
        exit(1)
    except FileNotFoundError:
        print('Path doesn\'t exist')
        exit(1)

    DEPTH = 0

    try:
        d = int(argv[2])
        if d >= 0:
            DEPTH = d
    except:
        None

    file_list = listdir()
    file_list.sort()
    print_dtree(DEPTH, file_list, 0)


if __name__ == '__main__':
    main()
