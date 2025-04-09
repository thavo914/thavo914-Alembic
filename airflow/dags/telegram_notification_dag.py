from airflow import DAG
from airflow.providers.telegram.operators.telegram import TelegramOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 4, 5),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    'telegram_notification',
    default_args=default_args,


    schedule_interval=None,
    catchup=False
)

# Replace these with your actual Telegram bot token and chat ID
telegram_token = '8186277751:AAFGs2a8Qhr52_dHpbsvlXOdQSr_lxctlhA'
telegram_chat_id = '1977848679'

send_message = TelegramOperator(
    task_id='send_telegram_message',
    telegram_conn_id='telegram_default',  # We'll create this connection
    chat_id=telegram_chat_id,
    text='Hello from Airflow! This is a test message.',
    dag=dag
)