from logging import Formatter
import gspread
from gspread.models import Spreadsheet
from oauth2client.service_account import ServiceAccountCredentials
from time import localtime, strftime

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name('service_account.json', scope)
client = gspread.authorize(credentials)

gc = gspread.service_account(filename='D:\WookieForce\service_account.json')

def get_time():
    return strftime("%a, %d %b %Y %H:%M:%S", localtime())

def simple_time():
    return strftime("%m/%d/%Y %I:%M %p", localtime()) + ' EST'

print(get_time() + ' - Program Start.')
sh = gc.open("Wookie Force Master Planning Sheet for CWLs and Classic Wars")


with open('fullroster.csv', 'r',encoding='utf-8') as file_obj:
    #print(chardet.detect(file_obj.read()))
    body = file_obj.read()
    body = body.encode('utf-8')
    client.import_csv(sh.id, data=body)

worksheet = sh.get_worksheet(0)
worksheet.format('A1:I1', {'textFormat': {'bold': True}})
print(get_time() + ' - Sheet added')