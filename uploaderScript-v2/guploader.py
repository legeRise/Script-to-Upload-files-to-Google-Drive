import os
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account

def upload_to_gdrive(title, file_path):
    # Path to your service account JSON key file
    service_account_file = "uploader_service_account.json"
    scopes = ['https://www.googleapis.com/auth/drive']

    # Authenticate using service account credentials
    credentials = service_account.Credentials.from_service_account_file(service_account_file, scopes=scopes)

    # Create Google Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Find the folder ID of the folder you shared with the service account
    folder_id = os.environ.get("DRIVE_FOLDER_ID")

    # Create a media file upload instance
    media = MediaFileUpload(file_path, mimetype='video/mp4')

    # Create a file metadata
    file_metadata = {
        'name': title,
        'parents': [folder_id]
    }

    # Upload the file to Google Drive
    uploaded_file = drive_service.files().create(
        body=file_metadata,
        media_body=media,
        fields='id'
    ).execute()

    # Get the file ID
    file_id = uploaded_file.get('id')

    # Construct the full link to the uploaded file
    full_link = f"https://drive.google.com/uc?id={file_id}"

    print("File uploaded successfully!")
    return full_link

title = input("Enter file title: ")
path = input("Enter file path: ")
link =upload_to_gdrive(title,path)
print("Follow the link to View ",link)