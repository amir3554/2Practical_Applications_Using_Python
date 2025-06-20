import gspread
from oauth2client.service_account import ServiceAccountCredentials
from google.oauth2.service_account import Credentials

scopes = [
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive'
]

credentials = Credentials.from_service_account_file("Keys.json", scopes=scopes)
file = gspread.authorize(credentials)#authorize(credentials)


# create new file

#new_file = file.create("A new SpSh from py")
###new_file.share("amirdwikat@example.com", perm_type='user', role='writer')

# ل اضافة الملف الى "ملفاتي " يجب وضع الرول الى اونر

#new_file.share("amirdwikat@example.com", perm_type='user', role='owner')
#في كل مرة نشغل البرنامج سوف ينشى لنا ملف جديد 


# open file

the_file = file.open("A new SpSh from py")

# creat new work sheet

###new_work_sheet = the_file.add_worksheet(title="Sheet_From_Py", rows=100, cols=20)
#سوف ينشء ورقة جديدة في كل مرة نشغل البرنامج 

work_sheet = the_file.worksheet("Sheet1")

work_sheet.update('A9:A9', [['Title']])

work_sheet.update_cell(10, 1, "Hello World!")

work_sheet.update('A1:C2', [[78 ,"rowan", 1300], [79, "hasan", 800] ])
 

