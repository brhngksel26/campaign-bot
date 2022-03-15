from driveServices import Create_Service

CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE,API_NAME,API_VERSION,SCOPES)

folders = ['alictus']

for folder in folders:
    file_metadata = {
        'name' : folder,
        'mineType' : 'application/vnd.google-apps.folder'
    }

    service.files().create(body=file_metadata).execute()