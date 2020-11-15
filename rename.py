""" rename.py is a utility to quickly rename photos and videos in name_i.format style. """

import os
import shutil
import glob2


def rename(file_format: str, path: str, name: str, i: int) -> None:
    """

    Function for quickly rename photos and videos in name_i.format style.

    Args:
        file_format (str): A variable that shows in which format to rename files.
        path (str): A variable in which the path to the files that will be renamed is stored.
        name (str): A variable that stores the name that will come before the file number.
        i (int): A variable that stores the start number of the file count.

    Returns:
        None: The function returns nothing.

    """
    for file in glob2.glob(f'*{file_format}'):
        i = str(i)
        shutil.move(f'{path}\\{file}', f'{path}\\{name}_{i}.{file_format}')
        i = int(i)
        i += 1


input_path = input('Path: ')

input_name = input('Name: ')

input_i = input('Number: ')

os.chdir(input_path)

rename('jpg', input_path, input_name, input_i)
rename('png', input_path, input_name, input_i)
rename('tif', input_path, input_name, input_i)
rename('gif', input_path, input_name, input_i)
rename('heic', input_path, input_name, input_i)
rename('mp4', input_path, input_name, input_i)
