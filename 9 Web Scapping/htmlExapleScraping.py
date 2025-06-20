import bs4
from pathlib import Path

file_html = open(Path.home()/ Path("Desktop", "tests", "example.html"))

noStarchSoup = bs4.BeautifulSoup(file_html, 'html.parser')
print(type(noStarchSoup))

element = noStarchSoup.select("#author")
element_paragraph = noStarchSoup.select("p")

print(element)
print(element[0].get_text())
print(element[0].attrs)

print(len(element_paragraph))
print(element_paragraph[0].get_text())
print(element_paragraph[1].get_text())
print(element_paragraph[2].get_text())