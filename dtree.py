from os import listdir
from os.path import isdir
from os import chdir
from sys import argv

IGNORE_LIST = [
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

FOLDER_COLOR = '\033[96m'
END_COLOR = '\033[0m'


def print_dtree(DEPTH, file_list, num):
    if num > DEPTH:
        return
    for file in file_list:
        if file in IGNORE_LIST:
            continue
        is_folder = isdir(file)
        if is_folder:
            print('├' + '─'*num + ' ' + FOLDER_COLOR + str(file) + END_COLOR)
        else:
            print('├' + '─'*num + ' ' + str(file))
        if(is_folder):
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
