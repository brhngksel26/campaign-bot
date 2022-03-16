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


def getSheetValue():
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    #sheetId = getSheetId(fileName)
    id = "1cwBp8Y4xzL5lJyg8gY11KIn_RJ9444d1t6EBcAwhkvM"

    data  = service.spreadsheets().values().get(
            spreadsheetId=id,
            range="A:F").execute()

    return data["values"]

def getCampaignValue(campaigns):
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    #sheetId = getSheetId(fileName)
    id = "1cwBp8Y4xzL5lJyg8gY11KIn_RJ9444d1t6EBcAwhkvM"

    data  = service.spreadsheets().values().get(
            spreadsheetId=id,
            range="A:F").execute()

    returnDataList = []

    for value in data["values"]:
        for campaign in campaigns:
            if str(value[0]) == str(campaign).upper():
                returnDataList.append(value)

    return returnDataList


def clearData():
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    #sheetId = getSheetId(fileName)
    id = "1cwBp8Y4xzL5lJyg8gY11KIn_RJ9444d1t6EBcAwhkvM"

    body = {
        "requests" : [
            {
                'updateCells' : {
                    'range': {
                        'sheetId' : id
                    },
                    'fields' : "*"
                }
            }
        ]
    }

    service.spreadsheets().batchUpdate(
        spreadsheetId=id,
        body=body
    ).execute()

def insertData():
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    #sheetId = getSheetId(fileName)
    id = "1MX0fopRIW5jweO6bnymnHigvjGiykXncE_gp7uG3gRA"

    valueData = getSheetValue()


    body = {
        'majorDimension' : "ROWS",
        "values" : valueData
    }

    service.spreadsheets().values().update(
        spreadsheetId=id,
        body=body,
        range= "A1",
        valueInputOption = 'USER_ENTERED'
    ).execute()


    pass

def updateColumns():
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    id = "1MX0fopRIW5jweO6bnymnHigvjGiykXncE_gp7uG3gRA"

    resource = {
        "majorDimension": "ROWS",
        "values": "=PRODUCT(C2;E2)"
    }

    formulaList = []
    test = []
    for i in range(2,15):
        formulaList.append(f"=PRODUCT(C{i};E{i})")

    body={"majorDimension": "ROWS", "values": formulaList}
    
    sheetRange = "G2:G14"
   
    service.spreadsheets().values().append(
        spreadsheetId=id,
        body=body,
        range=sheetRange
    ).execute()

#createSheet()
#print(getSheetValue("campaign.xlsx"))
#updateColumns()

"""tests = getSheetValue()
for test in tests:
    print(test)"""

insertData()

