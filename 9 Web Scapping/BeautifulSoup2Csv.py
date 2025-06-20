import bs4
import csv
import requests
from pathlib import Path

response = requests.get("https://en.wikipedia.org/wiki/List_of_languages_by_number_of_native_speakers")
soup = bs4.BeautifulSoup(response.text, "html.parser")

all_tables = soup.find_all("table")
filtered_tables = [table for table in all_tables if table.caption is not None]
the_table = None
for i in filtered_tables:
    if str(i.caption.text).strip() == 'Languages with at least 50 million first-language speakers[7]':
        the_table = i
        break
    else:
        print('bruh')
    
#print(str(the_table.caption.text).strip())


headers = [(header.text.replace('\n', '')) for header in (the_table.find_all('th'))]

#print(headers)


rows = the_table.find_all('tr')
data = []
for row in rows:
    the_data = [(d.text.replace('\n', '')) for d in (row.find_all('td'))]
    if len(the_data) == 0:
        continue
    data.append(the_data)

#print(data)


file = open(Path.home() / Path('Desktop', "tests", "BeautifulSoup.csv"), 'w', newline='')
writer = csv.writer(file)
writer.writerow(headers)
writer.writerows(data)
file.close()



