import gspread
from oauth2client.service_account import ServiceAccountCredentials

# نحدد نطاقات التطبيق
scopess = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]


credencialss = ServiceAccountCredentials.from_json_keyfile_name('keys.json',scopess)

file = gspread.authorize(credencialss)

sheet = file.open('test1').sheet1

sheet.update_cell(1,2, 'amir')

