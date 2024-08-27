import os
import time
import logging
from google.cloud import bigquery
from cims_ui import app
from cims_ui.page_helpers.google_utils import get_current_group, get_username

def load_csv_into_bigquery(file_uri, bq_dataset, bq_table):
    """Loads a CSV file into a BigQuery table.

    Args:
        file: The CSV file object to load.
    """
    start = time.time()
    project_name = app.config.get('GOOGLE_CLOUD_PROJECT_ID')
    bq_client = bigquery.Client()
    dataset = bigquery.Dataset(f'{project_name}.{bq_dataset}')
    dataset.location = "europe-west2"
    bq_client.create_dataset(dataset, exists_ok=True)

    table_id = f'{project_name}.{bq_dataset}.{bq_table}'
    # try:
    job = bq_client.load_table_from_uri(
        file_uri,
        table_id,
        job_config=bigquery.LoadJobConfig(
            source_format=bigquery.SourceFormat.CSV,
            skip_leading_rows=1,
            autodetect=True,
        )
    )
    job.result()  # Waits for the job to complete.
    logging.info(f'Loaded {job.output_rows} rows into {table_id}')
    logging.info(f'Time taken: {round(time.time() - start)} seconds')
        
    # except FileNotFoundError:
    #     logging.error(f'Error: File not found: {file}')
    # except Exception as e:
    #     logging.error(f"Error loading data into BigQuery: {e}")
    
    return table_id
