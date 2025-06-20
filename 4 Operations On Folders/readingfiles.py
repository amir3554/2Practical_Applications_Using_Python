import os
from pathlib import Path

print(os.getcwd())
print(Path.home())

MyFile = open(Path.home() / Path('Desktop', 'Python_2024_2025', 'Practical_Applications_Using_Python', 'operationsonfolders', 'file1.txt'), 'r')

#print(MyFile.read())

#print(MyFile.read(5))

#print(MyFile.readline())

lines = MyFile.readlines() # [its a list of lines]

print(lines[0:5])

for line in lines:
    print(line)

















