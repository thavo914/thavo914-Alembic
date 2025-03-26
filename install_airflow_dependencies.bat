@echo off
REM This batch file installs the dependencies in both airflow-webserver and airflow-scheduler containers

REM Copy requirements.txt to containers
echo Copying requirements.txt to airflow-webserver...
docker cp requirements-airflow.txt airflow-webserver:/opt/airflow/requirements.txt

echo Copying requirements.txt to airflow-scheduler...
docker cp requirements-airflow.txt airflow-scheduler:/opt/airflow/requirements.txt

REM First, check and install dependencies in the airflow-webserver container
echo Installing dependencies in airflow-webserver container...

docker exec -u airflow airflow-webserver bash -c "pip install --upgrade pip && pip install -r /opt/airflow/requirements.txt"

REM Check if installation in airflow-webserver was successful
if %errorlevel% neq 0 (
    echo Error installing dependencies in airflow-webserver.
    exit /b %errorlevel%
)

REM Now install dependencies in the airflow-scheduler container
echo Installing dependencies in airflow-scheduler container...
docker exec -u airflow airflow-scheduler bash -c "pip install --upgrade pip && pip install -r /opt/airflow/requirements.txt"

REM Check if installation in airflow-scheduler was successful
if %errorlevel% neq 0 (
    echo Error installing dependencies in airflow-scheduler.
    exit /b %errorlevel%
)

echo Dependencies installed successfully in both containers.

REM Optionally, restart the services after installation
echo Restarting airflow-webserver container...
docker restart airflow-webserver

echo Restarting airflow-scheduler container...
docker restart airflow-scheduler

echo Airflow containers restarted successfully.
pause
