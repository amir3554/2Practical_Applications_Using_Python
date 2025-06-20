from pathlib import Path


MyFile = open(Path.home() / Path('Desktop', 'Python_2024_2025', 'Practical_Applications_Using_Python', 'operationsonfolders', 'file2.txt'), 'w')
#, 'oprationsonfolders', 'file2.txt'), 'w')

MyFile.write("11 Hello im amir\n")
MyFile.write("12 Hello im amir\n")
MyFile.write("13 Hello im amir\n")
MyFile.close()


MyFile = open(Path.home() / Path('Desktop', 'Python_2024_2025', 'Practical_Applications_Using_Python', 'operationsonfolders', 'file2.txt'), 'a')
#, 'oprationsonfolders', 'file2.txt'), 'a')

MyFile.write("14 Hello im amir\n")
MyFile.write("15 Hello im amir\n")
MyFile.write("16 Hello im amir\n")
MyFile.close()
