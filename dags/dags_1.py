from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime as dt
from datetime import timedelta as td

def hello(name):
    print(f'Hallo {name} yang ganteng banget')

def kelas(name):
    print(f'{name} kelas berapa ya?')

def jawab(name):
    print(f'ternyata {name} kelassss')

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

dag = DAG(dag_id ='simple-dag',
          description ='Simple Python Dag', 
          default_args = default_args, 
          catchup = False,
          schedule = '*/6 * * * *',
          max_active_runs = 1, #BIAR DAG GA SELAP SELIP
          max_active_tasks = 2  #MAKS TASKS PARALLEL 2
          )

task_1 = PythonOperator(
    task_id='say_hello',
    python_callable=hello,
    op_args=['Dimas'],  # atau op_kwargs={'name': 'Dimas'}
    dag=dag
)

task_2 = PythonOperator(
    task_id='kelas',
    python_callable=kelas,
    op_args=['Dimas'],  # atau op_kwargs={'name': 'Dimas'}
    dag=dag
)

task_3 = PythonOperator(
    task_id='kelas_2',
    python_callable=jawab,
    op_args=['Dimas'],  # atau op_kwargs={'name': 'Dimas'}
    dag=dag
)

task_1 >> [task_2,task_3]