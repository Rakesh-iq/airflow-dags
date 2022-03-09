# Python standard modules
from datetime import datetime, timedelta# Airflow modules
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'Rakesh',
    'depends_on_past': False,
    # Start on 27th of June, 2020
    'start_date': datetime(2022,2, 24),
    'email': ['airflow@example.com '],
    'email_on_failure': False,
    'email_on_retry': False,
    # In case of errors, do one retry
    'retries': 1,
    # Do the retry with 30 seconds delay after the error
    'retry_delay': timedelta(seconds=30),
    # Run once every 5 minutes
    # 'schedule_interval': '*/5 * * * *'
}

with DAG(dag_id='simple_bash_dag_test',
    default_args=default_args,  
    schedule_interval=timedelta(days=1),
    tags=['my_dags'],
) as dag:    #Here we define our first task
    t1 = BashOperator(bash_command="touch /tmp/file1.txt", task_id="create_file")    #Here we define our second task
    t2 = BashOperator(bash_command="mv /tmp/file1.txt /tmp/file_1.txt", task_id="change_file_nam")    # Configure T2 to be dependent on T1’s execution
    t3 = BashOperator(bash_command="ls /tmp", task_id="list_files")    #Here we define our second task

    t1 >> t2 # >> t3