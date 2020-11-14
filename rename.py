""" rename.py is a utility to quickly rename photos
    and videos in name_i.format style. """

import os
import shutil
import glob2

path = input('Путь: ')

name = input('Имя: ')

i = '1'

os.chdir(path)

files = os.listdir()

for file in glob2.glob("*jpg"):
    i = str(i)
    shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.jpg')
    i = int(i)
    i += 1

for file in glob2.glob("*png"):
    i = str(i)
    shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.png')
    i = int(i)
    i += 1

for file in glob2.glob("*tif"):
    i = str(i)
    shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.tif')
    i = int(i)
    i += 1

for file in glob2.glob("*gif"):
    i = str(i)
    shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.gif')
    i = int(i)
    i += 1

for file in glob2.glob("*heic"):
    i = str(i)
    shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.heic')
    i = int(i)
    i += 1

for file in glob2.glob("*mp4"):
    shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.mp4')
    i = int(i)
    i += 1
