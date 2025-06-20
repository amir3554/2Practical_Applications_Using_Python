import gspread
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive']

credentials = Credentials.from_service_account_file('keys.json',scopes=scopes)

file = gspread.authorize(credentials)

sheet = file.open('test1').sheet1

#sheet.batch_clear(["I3:I3"])

sheet.update_cell(9, 3, "=SUM(C2:C8)")

sheet.update_cell(10, 3, "=MAX(C2:C8)")

sheet.update_cell(11, 3, "=AVARAGE(C2:C8)")

cell = sheet.acell("C11", value_render_option="FORMULA").value

print(cell)

