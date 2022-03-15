from driveServices import Create_Service

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def createSheet():
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    sheet_body = {
        'properties' : {
            'title'  : 'campaign-bot',
        }
    }

    sheets_file = service.spreadsheets().create(
        body=sheet_body
    ).execute()



def getSheetId(fileName):
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    file_service = service.spreadsheets()
    print(dir(file_service))
    print(file_service.get(name=fileName))
    results = file_service.get(fields="files(id, name)").execute()
    file_list = results.get('files')
    for file in file_list:
        if file['name'] == fileName:
            return file['id']


def getSheetValue(fileName):
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    #sheetId = getSheetId(fileName)
    id = "1cwBp8Y4xzL5lJyg8gY11KIn_RJ9444d1t6EBcAwhkvM"

    data  = service.spreadsheets().values().get(
            spreadsheetId=id,
            majorDimension="ROWS",
            range="A1:F6").execute()

    return data["values"]


#createSheet()
#print(getSheetId("campaign.xlsx"))
tests = getSheetValue("campaign.xlsx")
for test in tests:
    print(test)



