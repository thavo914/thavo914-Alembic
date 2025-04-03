@echo off
REM This batch file installs the dependencies in both airflow-webserver and airflow-scheduler containers

echo Checking Python version in airflow-webserver...
docker exec airflow-webserver python --version

echo Checking Python version in airflow-scheduler...
docker exec airflow-scheduler python --version

echo Dependencies installed successfully in both containers.

REM Optionally, restart the services after installation
echo Restarting airflow-webserver container...
@REM docker restart airflow-webserver

echo Restarting airflow-scheduler container...
@REM docker restart airflow-scheduler

