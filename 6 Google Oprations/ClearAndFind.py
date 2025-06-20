import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file("Keys.json", scopes=scopes)

file = gspread.authorize(credentials)

the_file = file.open("A new SpSh from py")

sheet = the_file.sheet1

# find 

cell = sheet.find("rawan")
print(f"Found something at row:{cell}, colomn {cell}")

cell2 = sheet.findall("hasan")
print(cell2)
