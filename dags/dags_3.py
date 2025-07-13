from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime as dt
from datetime import timedelta as td

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

with DAG(dag_id ='loop_test',
          description ='Simple Pandas Python Dag', 
          default_args = default_args, 
          catchup = False,
          schedule = None,
          max_active_runs = 1, #BIAR DAG GA SELAP SELIP
          max_active_tasks = 2  #MAKS TASKS PARALLEL 2
          ) as dag :
    
    tasks = []
    for x in range(5):
        task = BashOperator(
            task_id = f'task_{x}',
            bash_command = 'echo Hallo {{ dag.owner }}, ini dari {{ task.task_id }}'
        )

        tasks.append(task)
    
    task_last = BashOperator(
        task_id = 'tampil_csv',
        bash_command = 'tail -n 10 "$file_path"',
        env = {'file_path' : '/opt/airflow/include/data/transactions.csv'}
    )
    
    tasks[0] >> tasks[1] >> tasks[2] >> tasks[3] >> tasks[4] >> task_last