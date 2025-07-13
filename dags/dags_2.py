from airflow import DAG
from airflow.operators.python import PythonOperator
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from utils import ETL


default_args = {
    'owner' : 'Dimas Ega Ganteng Parah',
    'start_date' : dt(2025,5,27),
    'depends_on_past' : False,
    'email' : 'dimasega1811@gmail.com',
    'email_on_failure' : True,
    'email_on_retry' : False,
    'retries' : 1,
    'retry_delay' : td(minutes= 2),
}

def run_etl(file_input, file_output):
    etl = ETL.ETLPipeline(file_input,file_output)
    etl.run()


dag = DAG(dag_id ='csv_dag',
          description ='Simple Pandas Python Dag', 
          default_args = default_args, 
          catchup = False,
          schedule = None,
          max_active_runs = 1, #BIAR DAG GA SELAP SELIP
          max_active_tasks = 2  #MAKS TASKS PARALLEL 2
          )

task_1 = PythonOperator(
    task_id='extract_csv',
    python_callable=run_etl,
    op_args=['/opt/airflow/include/data/transactions.csv','/opt/airflow/include/data/transactions_cleaned.csv'],
    dag=dag,
    execution_timeout=td(minutes=10)
)

task_1