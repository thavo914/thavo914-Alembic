from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.email_operator import EmailOperator
from datetime import datetime, timedelta

# Default arguments common to all tasks in the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2025, 4, 11),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'email': ['thangvo0914@gmail.com'],  # Add your email
    'email_on_failure': True,
    'email_on_retry': True,
}

# -- Modular Task Functions --

def extract_data(**kwargs):
    """
    Extract Data Task:
    Simulates data extraction by returning a list of numbers.
    """
    data = [1, 2, 3, 4, 5]
    print("Extracted data:", data)
    # Pushing data to XCom for downstream tasks
    return data

def transform_data(**kwargs):
    """
    Transform Data Task:
    Retrieves the data extracted from the previous task,
    doubles each element, and returns the transformed dataset.
    """
    # Pull data from the 'extract_data_task' via XCom
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='extract_data_task')
    
    if data is None:
        raise ValueError("No data found from extract_data_task")
    
    transformed_data = [x * 2 for x in data]
    print("Transformed data:", transformed_data)
    return transformed_data

def load_data(**kwargs):
    """
    Load Data Task:
    Retrieves the transformed data and simulates loading it to a destination.
    """
    # Pull data from the 'transform_data_task' via XCom
    ti = kwargs['ti']
    transformed_data = ti.xcom_pull(task_ids='transform_data_task')
    
    if transformed_data is None:
        raise ValueError("No transformed data found from transform_data_task")
    
    print("Loading data:", transformed_data)
    # Simulate a loading step, e.g., writing to a database or a file
    print("Data loaded successfully")

# -- Define the DAG using code-as-configuration --

with DAG(
    'data_pipeline_example',
    default_args=default_args,
    description='An example DAG demonstrating code-as-configuration with email notifications',
    schedule_interval=timedelta(days=1),
    catchup=False
) as dag:

    # Create the extract task
    extract_data_task = PythonOperator(
        task_id='extract_data_task',
        python_callable=extract_data,
        provide_context=True,
        doc_md="""\
### Extract Data Task
Extracts data from a simulated source and pushes the data to XCom.
        """
    )

    # Create the transform task
    transform_data_task = PythonOperator(
        task_id='transform_data_task',
        python_callable=transform_data,
        provide_context=True,
        doc_md="""\
### Transform Data Task
Transforms the data extracted by doubling each element. 
Retrieves data via XCom and pushes the transformed data back to XCom.
        """
    )

    # Create the load task
    load_data_task = PythonOperator(
        task_id='load_data_task',
        python_callable=load_data,
        provide_context=True,
        doc_md="""\
### Load Data Task
Simulates loading the transformed data into a destination system.
It retrieves the data via XCom and logs the loading process.
        """
    )

    # Define task dependencies (modular DAG design)
    # Add success email notification
    email_success = EmailOperator(
        task_id='send_success_email',
        to=default_args['email'],
        subject='Data Pipeline Completed Successfully',
        html_content="""
        <h3>Data Pipeline Execution Report</h3>
        <p>The data pipeline has completed successfully.</p>
        <p>Execution date: {{ ds }}</p>
        <p>View the task logs in Airflow for more details.</p>
        """,
        dag=dag
    )

    # Update task dependencies to include email notification
    extract_data_task >> transform_data_task >> load_data_task >> email_success
