from PyPDF2 import PdfWriter as w
import PyPDF2 
from pathlib import Path

# Create
pdf = w()

file = open(Path.home() / Path("Desktop", "tests", "FromPy.pdf"), "wb")

for i in range(5):
    pdf.add_blank_page(219, 297)

pdf.write(file)


# Copy

The_file = open(Path.home() / Path("Desktop", "tests", "PythonHeaders.pdf"), "rb")

the_content = PyPDF2.PdfReader(The_file)

for pagesNUM in range(len(the_content.pages)):
    The_page = the_content.pages[pagesNUM]
    pdf.add_page(The_page)

pdf.write(file)

The_file.close()
