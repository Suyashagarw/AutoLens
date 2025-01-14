
import apps, base64, requests
import os, string, random, glob
from flask import json
from werkzeug.utils import secure_filename
from apps.services.s3Manager.routes import s3_upload, s3_delete_all

def upload_file(file):
    print(file)
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(32)) + secure_filename(file.filename)
    apps.logger.info(filename)

    bucket_name=apps.STORAGE_BUCKET
    # s3_upload(bucket_name, file, filename)
    print(file)
    response = s3_upload(bucket_name, file, filename)

    print(response)
    return response["data"]

def removeAllImages():
    bucket_name=apps.STORAGE_BUCKET
    return s3_delete_all(bucket_name)
    
