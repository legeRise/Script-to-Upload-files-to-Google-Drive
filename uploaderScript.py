from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from oauth2client.service_account import ServiceAccountCredentials
import os

# Path to your service account JSON key file
service_account_file = 'uploader_service_account.json'
scopes=['https://www.googleapis.com/auth/drive']
# Authenticate using service account credentials
credentials = ServiceAccountCredentials.from_json_keyfile_name(service_account_file,scopes )
# Initialize GoogleAuth
gauth = GoogleAuth()

# Use the credentials to authenticate with PyDrive
gauth.credentials = credentials

# Create GoogleDrive instance
drive = GoogleDrive(gauth)

# Specify the file you want to upload
file_path = 'test.mp4'

# Find the folder ID of the folder you shared with the service account
folder_id = os.environ.get("gdrive_folder_id")

# Create a GoogleDriveFile instance
file = drive.CreateFile({'title': 'final1.mp4','mimeType': 'video/mp4',  'parents': [{'id': folder_id}]})

# Set the content of the file
file.SetContentFile(file_path)

# Upload the file to Google Drive
file.Upload()

print("File uploaded successfully!")
