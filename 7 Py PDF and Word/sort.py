from PyPDF2 import PdfWriter as w
from PyPDF2 import PdfReader as r
from pathlib import Path
from os import listdir

write_to_file = w()

file = open(Path.home() / Path("Desktop", "tests", "AllHeadersPy2.pdf"), "wb")
files = listdir(Path.home() / Path("Desktop", "tests"))
files_pdf_only = []

for i_file in files:
    if "Header" in i_file and i_file.endswith("pdf"):
        files_pdf_only.append(i_file)

files_pdf_only.sort()
files_pdf_only.remove('AllHeadersPy.pdf' )
files_pdf_only.remove('AllHeadersPy2.pdf')
# print(files_pdf_only) >>> ['1PythonHeaders.pdf', '2PythonHeaders.pdf', '3PythonHeaders.pdf', 'AllHeadersPy.pdf']

for i in files_pdf_only:
    the_file =  open(Path.home() / Path("Desktop", "tests", f"{i}"), "rb")
    the_content = r(the_file)
    for pageNUM in range(len(the_content.pages)):
        The_page = the_content.pages[pageNUM]
        #if The_page == the_content.pages[0]:
        #    continue
        #else:
        write_to_file.add_page(The_page) 

write_to_file.write(file)
file.close()
the_file.close()







