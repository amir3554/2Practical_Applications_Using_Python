import gspread
from oauth2client.service_account import ServiceAccountCredentials


scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credencials = ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopes)

file = gspread.authorize(credencials)

file.open('test1')
sheet = file.open_by_url('https://docs.google.com/spreadsheets/d/1QcEFK_FW7tj0KAibcUx-HFXIpDWJoYgNE1Q1kOvBGu4/edit?usp=drive_link')

sheet0 = sheet.get_worksheet(0)

sheet5 = sheet.worksheet('Sheet5')

sheets = sheet.worksheets()

print(sheets)


val1 =  sheet0.acell("B2").value
print(val1)

val2 = sheet0.cell(5, 3).value
print(val2)

row3_list = sheet0.row_values(4)
print(row3_list)

col2_list = sheet0.col_values(2)
print(col2_list)

print("------------------------------------------------------------")

#لطباعة جميع السجلات و كل سجل على حدى في قائمة

list_of_lists = sheet0.get_all_values()
print(list_of_lists)

print("------------------------------------------------------------")

list_of_dicts = sheet0.get_all_records()
print(list_of_dicts)

print("------------------------------------------------------------")





