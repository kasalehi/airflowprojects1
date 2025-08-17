from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime ,timedelta
import json
import requests
from pathlib import Path

from files import _get_pictures

dag= DAG(
    dag_id='my_dag',
    start_date=datetime(2023, 1, 1),
    catchup=False
)
# read data from url 



download_launches = BashOperator(
    task_id="download_launches",
    bash_command="curl -o /tmp/launches.json -L 'https://ll.thespacedevs.com/2.0.0/launch/upcoming'",  # noqa: E501
    dag=dag,
)




                
                
get_pictures = PythonOperator(
    task_id="get_pictures", 
    python_callable=_get_pictures, 
    dag=dag
)



notify = BashOperator(
    task_id="notify",
    bash_command="echo 'Images have been downloaded'",
    dag=dag
)


download_launches >> get_pictures >> notify