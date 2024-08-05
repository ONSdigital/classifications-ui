import os
import time
from google.cloud import bigquery
from cims_ui import app

def load_csv_into_bigquery(file):
    """Loads a CSV file into a BigQuery table.

    Args:
        file: The CSV file object to load.
    """
    start = time.time()
    client = bigquery.Client()
    project_id = app.config.get('GOOGLE_CLOUD_PROJECT_ID')
    bq_dataset = app.config.get('BQ_DATASET')
    bq_table = app.config.get('BQ_TABLE')
    table_id = f'{project_id}.{bq_dataset}.{bq_table}.{start}' 
    try:
        with open(file, 'rb') as source_file:
            job = client.load_table_from_file(
                source_file,
                table_id, 
                job_config=bigquery.LoadJobConfig(
                    source_format=bigquery.SourceFormat.CSV,
                    skip_leading_rows=1,
                    autodetect=True,
                )
            )
            job.result()  # Waits for the job to complete.
        print(
            "Loaded {} rows into {}.".format(job.output_rows, table_id),
            end=' ',
        )
        print(f"Time taken: {time.time() - start} seconds")
        
    except FileNotFoundError:
        print(f"Error: File not found: {file}")
    except Exception as e:
        print(f"Error loading data into BigQuery: {e}")
    
    return table_id
