from google.cloud import storage
from cims_ui import app
from cims_ui.page_helpers.google_utils import get_current_group, get_username
import logging
import time
import uuid

def upload_to_cs(file):
    bucket_obj = _get_bucket()
    new_filename, time_ref = _create_new_filename()
    file_uri = _load_csv_to_bucket(file, new_filename, bucket_obj)
    return file_uri, time_ref

def _get_bucket():
    storage_client = storage.Client()
    bucket_name = app.config.get('BUCKET_NAME')
    bucket_obj = storage_client.bucket(bucket_name)
    return bucket_obj

def _create_new_filename():
    time_identifier_unique = f'in_{round(time.time())}_{uuid.uuid4()}'
    username = get_username()
    new_filename = f'{username}_{time_identifier_unique}.csv'
    return new_filename, time_identifier_unique

def _load_csv_to_bucket(file, new_filename, bucket_obj):
    blob_obj = bucket_obj.blob(new_filename)
    blob_obj.upload_from_file(file)
    file_uri = f'gs://{bucket_obj.name}/{new_filename}'
    return file_uri