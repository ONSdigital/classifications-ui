"""FLASK DEVEOPMENT CONFIG"""
import os

SECRET_KEY = b'secretkey'
# API_URL = os.getenv('API_URL')

GOOGLE_CLOUD_PROJECT_ID = os.getenv('GOOGLE_CLOUD_PROJECT_ID')
BQ_DATASET = os.getenv('BQ_DATASET')
BQ_TABLE = os.getenv('BQ_TABLE')
