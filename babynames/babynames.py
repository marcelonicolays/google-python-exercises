#!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re
import textwrap
"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""
def extract_year(filename):
    with open(filename) as f:
        file = f.read()
    year = re.search(r'Popularity in .*([\d]{4})', file).group(1)

    return year



def extract_names(filename):
    """
    Given a file name for baby.html, returns a list starting with the year string
    followed by the name-rank strings in alphabetical order.
    ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
    """
    # +++your code here+++
    names = []
    with open(filename) as f:
        file = f.read()

    name = re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', file)
    for item in name:
        names.append(item[1] + ' ' + item[0])
        names.append(item[2] + ' ' + item[0])

    return names

def dict_names(filename):
    names = extract_names(filename)
    d_names = {}
    for x in names:
        y = x.split()
        d_names[y[0]] = y[1]
    return d_names

def call_names(filename):
    d_names = dict_names(filename)
    c_name = input('Digite o nome: ')
    names = extract_names(filename)
    list = []
    for x in names:
        y = x.split()
        list.append(y[0])
    lista = sorted(list)
    while c_name.title() not in d_names:
        print(textwrap.fill(','.join(lista), 100))
        print('Name not in the list of most registered')
        c_name = input('Digite outro nome: ')
    return c_name.title()



def main():
    # This command-line parsing code is provided.
    # Make a list of command line arguments, omitting the [0] element
    # which is the script itself.
    print('Consulte um nome entre os mais regisrtados por ano.')
    args = sys.argv[1:]
    c_year = input('digite o ano desejado: ')
    file = 'baby%s.html' %(c_year)
    y_available = ('1990', '1992', '1994', '1996', '1998', '2000', '2002', '2004', '2006', '2008')
    while c_year not in y_available:
        print('Year not available, please chose one of this list: ')
        print(y_available)
        c_year = input('Digite o ano desejado: ')
        file = 'baby%s.html' % (c_year)

    #if not args:
    #    print('usage: [--summaryfile] file [file ...]')
    #   sys.exit(1)

    # Notice the summary flag and remove it from args if it is present.
    #summary = False
    #if args[0] == '--summaryfile':
    #    summary = True
    #    del args[0]

        # +++your code here+++
        # For each filename, get the names, then either print the text output
        # or write it to a summary file

    year = extract_year(file)
    names = extract_names(file)
    d_names = dict_names(file)
    name = call_names(file)
    #print(year)
    #print(names)
    #print(d_names)
    #list = []
    #list.append(year)
    #list = list + sorted(names)

    print('In %s the name %s was the %s most registered.' % (year, name, d_names[name]))
    #print(list)

if __name__ == '__main__':
    main()
