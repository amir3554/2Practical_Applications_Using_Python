import bs4
import requests


# https://fortnitedb.com/
# #hnrtb > tbody > tr:nth-child(10) > td.cell.col.epic--border-small
# #hnrtb > tbody > tr:nth-child(10) > td.cell.col.epic--border-small > img
# body > main > div.container.pt-2 > div:nth-child(1) > div.col-12 > div.view > div


res = requests.get('https://fortnitedb.com/')
#print(res.text)


noStarchSoup = bs4.BeautifulSoup(res.text, "html.parser")
print(type(noStarchSoup))

element = noStarchSoup.select('body > main > div.container.pt-2 > div:nth-child(1) > div.col-12 > div.view > div > div')

print(element)
#print(element[0].get_text())
