from os import listdir
from os.path import isdir
from os import chdir
from sys import argv

DEPTH = 0

try:
    folder_path = argv[1]
    chdir(folder_path)
except IndexError:
    print('No path found')
    exit(1)
except FileNotFoundError:
    print('Path doesn\'t exist')
    exit(1)

try:
    DEPTH = int(argv[2])
except:
    None

file_list = listdir()


def print_file_list(file_list, num):
    if num > DEPTH:
        return
    for file in file_list:
        if file == '.git' or file == 'node_modules' or file == 'build':
            continue
        print('-'*num + str(file))
        if(isdir(file)):
            chdir(file)
            print_file_list(listdir(), num+1)
            chdir('../')
        if num == 0 and DEPTH > 0:
            print("")


print_file_list(file_list, 0)
