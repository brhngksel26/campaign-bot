from driveServices import Create_Service
from googleapiclient.http import MediaFileUpload

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']


def createFolder():

    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

    folders = ['alictus']

    for folder in folders:
        file_metadata = {
            'name' : folder,
            'mimeType' : 'application/vnd.google-apps.folder'
        }

        service.files().create(body=file_metadata).execute()

def getFolder():
    page_token = None
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    while True:
        response = service.files().list(q="mimeType='application/vnd.google-apps.folder'",
                                            
                                            fields='nextPageToken, files(id, name)',
                                            pageToken=page_token).execute()
        for file in response.get('files', []):
            # Process change
            print ('Found file: %s (%s)' % (file.get('name'), file.get('id')))
        page_token = response.get('nextPageToken', None)


def listFolders(folderName):
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    resource = service.files()
    results = resource.list( fields="files(id, name)").execute()
    file_list = results.get('files')
    for file in file_list:
        if file['name'] == folderName:
            return file['id']


def uploadFile(folderName):
    service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)
    folder_id = listFolders(folderName)
    file_names = ["campaign.xlsx"]
    mine_types = ["application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"]

    for file_name,mine_type in zip(file_names,mine_types):
        file_metadata = {
            'name' : file_name,
            'parents' : [folder_id]
        }

        media = MediaFileUpload(f"C:/Users/burhan.goksel/Documents/github/campaign-bot/{file_name}",mimetype=mine_type)

        service.files().create(
            body=file_metadata,
            media_body=media,
            fields = 'id'
        ).execute()


#print((listFolders("alictus")))

#createFolder()
uploadFile("alictus")