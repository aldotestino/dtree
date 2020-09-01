from os import listdir
from os.path import isdir
from os import chdir
from sys import argv

try:
    folder_path = argv[1]
    chdir(folder_path)
except IndexError:
    print('No path found')
    exit(1)
except FileNotFoundError:
    print('Path doesn\'t exist')
    exit(1)


file_list = listdir()


def print_file_list(file_list, sign):
    for file in file_list:
        if file == '.git' or file == 'node_modules' or file == 'build':
            return
        print(sign + str(file))
        if(isdir(file)):
            chdir(file)
            print_file_list(listdir(), sign*2)
            chdir('../')


print_file_list(file_list, '-')
