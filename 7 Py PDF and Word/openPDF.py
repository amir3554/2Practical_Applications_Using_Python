import openPDF
import PyPDF2
from pathlib import Path

file = PyPDF2.PdfReader(Path.home() / Path("Desktop", "tests", "PythonHeaders.pdf"))

print(len(file.pages))
page1 = file.pages[0]

print(page1.extract_text())



