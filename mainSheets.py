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
            range="A:F").execute()

    return data["values"]


def updateColumns():
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    id = "1MX0fopRIW5jweO6bnymnHigvjGiykXncE_gp7uG3gRA"

    request_body = {
    'requests': [
        {
            'updateCells': {
                'rows': {
                    'values': [
                        {
                            'pivotTable': {
                                # Data Source
                                'source': {
                                    'sheetId': '0',
                                    'startRowIndex': 1,
                                    'startColumnIndex': 0,
                                    'endRowIndex': 14,
                                    'endColumnIndex': 7 # base index is 1
                                },
                                
                                # Rows Field(s)
                                'rows': [
                                    # row field #1
                                    {
                                        'sourceColumnOffset': 1,
                                        'showTotals': True, # display subtotals
                                        'sortOrder': 'ASCENDING',
                                        'repeatHeadings': True,
                                        'label': 'Country List',
                                    }
                                ],

                                # Columns Field(s)
                                'columns': [
                                    # column field #1
                                    {
                                        'sourceColumnOffset': 14,
                                        'sortOrder': 'ASCENDING', 
                                        'showTotals': True
                                    }
                                ],

                                # Values Field(s)
                                'values': [
                                    # value field #1
                                    {
                                        'summarizeFunction': 'CUSTOM',
                                        'sourceColumnOffset': 7,
                                        'name': '=C*E '
                                    }
                                ],

                                'valueLayout': 'HORIZONTAL'
                            }
                        }
                    ]
                },
                
                'start': {
                    'sheetId': '0',
                    'rowIndex': 1, # 4th row
                    'columnIndex': 6 # 3rd column
                },
                'fields': 'pivotTable'
            }
        }
    ]
}
   
    response = service.spreadsheets().batchUpdate(
        spreadsheetId=id,
        body=request_body
    ).execute()

#createSheet()
#print(getSheetId("campaign.xlsx"))
updateColumns()

"""tests = getSheetValue("campaign.xlsx")
for test in tests:
    print(test)"""



