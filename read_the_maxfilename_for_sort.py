import os
import pathlib
from os import listdir
from os.path import isfile, join

def max_number():
    my_path = pathlib.Path().absolute()
    filename = [f for f in listdir(path=my_path) if isfile(join(my_path,f))]

    num = []
    for i in filename:
        j = i.split('.')[0]
        k = int(j)
        num.append(k)

    max = 0
    for l in num:
        if l > max:
            max = l
        else:
            continue
    return max + 1

if __name__ == "__main__":
    max_number()