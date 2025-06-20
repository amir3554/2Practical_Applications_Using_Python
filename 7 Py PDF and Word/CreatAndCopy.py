import PyPDF2 
from pathlib import Path

# Create

file = open(Path.home() / Path("Desktop", "tests", "FromPy.pdf"), "wb")

for i in range(5):
    PyPDF2.PdfWriter().add_blank_page(219, 297)

PyPDF2.PdfWriter().write(file)


# Copy

The_file = open(Path.home() / Path("Desktop", "tests", "PythonHeaders.pdf"), "rb")

the_content = PyPDF2.PdfReader(The_file)

for pagesNUM in range(len(the_content.pages)):
    The_page = the_content.pages[pagesNUM]
    PyPDF2.PdfWriter().add_page(The_page)

PyPDF2.PdfWriter().write(file)

The_file.close()
