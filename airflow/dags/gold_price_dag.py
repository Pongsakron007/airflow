from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from plugins.fetch import fetch
from plugins.load import load
#import sys
#import os
#sys.path.append('/opt/airflow/plugins')

with DAG(
    dag_id="gold_price_etl",
    start_date=datetime(2023, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    fetch_price = PythonOperator(
        task_id='fetch_price',
        python_callable=fetch
    )

    save_price = PythonOperator(
        task_id='save_to_db',
        python_callable=load,
        provide_context=True
    )

    fetch_price >> save_price

###