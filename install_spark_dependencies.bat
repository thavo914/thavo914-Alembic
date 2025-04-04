@echo off
REM This batch file installs Java and dependencies in Spark containers

echo Checking Python version in spark-master...
docker exec spark-master python3 --version
docker exec spark-master pip3 --version

echo Checking Python version in spark-worker...
docker exec spark-worker python3 --version
docker exec spark-worker pip3 --version

echo Installing Python dependencies...
docker cp requirements-spark.txt spark-master:/opt/bitnami/spark/requirements.txt
docker exec -u root spark-master pip3 install -r /opt/bitnami/spark/requirements.txt

echo Setting PYSPARK_PYTHON and PYSPARK_DRIVER_PYTHON in containers...
docker exec -u root spark-master bash -c "echo 'export PYSPARK_PYTHON=/usr/bin/python3' >> /opt/bitnami/spark/conf/spark-env.sh"
docker exec -u root spark-master bash -c "echo 'export PYSPARK_DRIVER_PYTHON=/usr/bin/python3' >> /opt/bitnami/spark/conf/spark-env.sh"
docker exec -u root spark-worker bash -c "echo 'export PYSPARK_PYTHON=/usr/bin/python3' >> /opt/bitnami/spark/conf/spark-env.sh"
docker exec -u root spark-worker bash -c "echo 'export PYSPARK_DRIVER_PYTHON=/usr/bin/python3' >> /opt/bitnami/spark/conf/spark-env.sh"

echo Verifying PySpark configuration...
docker exec spark-master bash -c "source /opt/bitnami/spark/conf/spark-env.sh && echo PYSPARK_PYTHON=$PYSPARK_PYTHON"
docker exec spark-master bash -c "source /opt/bitnami/spark/conf/spark-env.sh && echo PYSPARK_DRIVER_PYTHON=$PYSPARK_DRIVER_PYTHON"

echo Verifying Python packages...
docker exec spark-master pip3 list | findstr requests

echo Installation completed successfully.
pause