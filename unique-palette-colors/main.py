# should take a PAL file and find all values of R, G and B that i duplicate

import sys

from pal_manager import PalManager 

FILENAME = ''

if(len(sys.argv) < 2):
    print('Please provide a filename!')
    quit()

FILENAME = sys.argv[1]

file_lines = []

with open(FILENAME, 'r') as file:
    for line in file:
        file_lines.append(line.rstrip('\n'))


pal_manager = PalManager(file_lines[2])

for rgb in file_lines[3:]:
    pal_manager.add_value(rgb)

pal_manager.print()
