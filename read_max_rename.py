import os
import pathlib
from os import listdir
from os.path import isfile, join
my_path = pathlib.Path().absolute()
filename = [f for f in listdir(path=my_path) if isfile(join(my_path,f))]
def max_number():    
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
    return max

def rename(max):
    count = max
    for i in filename:
        if '.jpg' in i:
            os.rename(i,'{}.jpg'.format(str(count)))
            count +=1

if __name__ == "__main__":
    max = max_number()
    rename(max)