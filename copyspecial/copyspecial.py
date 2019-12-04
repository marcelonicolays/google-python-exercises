#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Problem description:
# https://developers.google.com/edu/python/exercises/copy-special


import os
import shutil
import sys
import re
from zipfile import ZipFile

"""Copy Special exercise
The copyspecial.py program takes one or more directories as its arguments. We'll say that a "special" 
file is one where the name contains the pattern __w__ somewhere, where the w is one or more word chars. 
The provided main() includes code to parse the command line arguments, but the rest is up to you. 
Write functions to implement the features below and modify main() to call your functions.

Suggested functions for your solution(details below):

get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory
copy_to(paths, dir) given a list of paths, copies those files into the given directory
zip_to(paths, zippath) given a list of paths, zip those files up into the given zipfile

Part A (manipulating file paths)

Gather a list of the absolute paths of the special files in all the directories. In the simplest case, 
just print that list (here the "." after the command is a single argument indicating the current directory). 
Print one absolute path per line.
We'll assume that names are not repeated across the directories 
(optional: check that assumption and error out if it's violated).


Part B (file copying)

If the "--todir dir" option is present at the start of the command line, 
do not print anything and instead copy the files to the given directory, creating it if necessary. 
Use the python module "shutil" for file copying

Part C (calling an external program)
If the "--tozip zipfile" option is present at the start of the command line, 
run this command: "zip -j zipfile <list all the files>". This will create a zipfile containing the files. 
Just for fun/reassurance, also print the command line you are going to do first (as shown in lecture). 



"""


# +++your code here+++
# Write functions and modify main() to call them
def get_special_path(dir):
    special_files = []
    special_path = []
    path = os.listdir(dir)
    for x in path:
        match = re.search(r'[\w]*__[\w]*__[\w]*.[\w]*', str(x))
        if match:
            special_files.append(match.group())
    for y in special_files:
        special_path.append(os.path.abspath(os.path.join(dir, y)))

    #print('\n'.join(special_path))
    return special_path


def copy_to(path, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    for files in path:
        shutil.copy(files, dest_dir)
        #print('copy...', files)
    #print('successfuly copied files')

def zip_to(path, zippath):
    print('Following files will be zipped: ')
    for files in path:
        print(files)
    with ZipFile(zippath, 'w') as zip:
        for file in path:
            zip.write(file)
    print('All file zipped successfully!')


def main():
    # This basic command line argument parsing code is provided.
    # Add code to call your functions below.

    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    args = sys.argv[1:]
    if not args:
        print("usage: [--todir dir][--tozip zipfile] dir [dir ...]")
        sys.exit(1)

    # todir and tozip are either set from command line
    # or left as the empty string.
    # The args array is left just containing the dirs.
    todir = ''
    tozip = ''
    if args[0] == '--todir':
        todir = args[1]
        del args[0:2]
    elif args[0] == '--tozip':
        tozip = args[1]
        del args[0:2]
    else:
        print('error 3')

    if len(args) == 0:
        print("error: must specify one or more dirs")
        sys.exit(1)


    special_path = get_special_path(args[0])

    if todir:
        copy_to(special_path, todir)
    else:
        if tozip == False:
            print('error: 1')

    if tozip:
        zip_to(special_path, tozip)
    else:
        if todir == False:
            print('error 2')


        # +++your code here+++
        # Call your functions


if __name__ == "__main__":
    main()
