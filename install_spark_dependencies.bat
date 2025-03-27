@echo off
REM This batch file installs Java and dependencies in Spark containers

REM Install Java 11 in spark-master
echo Installing Java 11 in spark-master...
docker exec -u root spark-master bash -c "apt-get update && apt-get install -y openjdk-11-jdk && apt-get clean && rm -rf /var/lib/apt/lists/*"

REM Install Java 11 in spark-worker
echo Installing Java 11 in spark-worker...
docker exec -u root spark-worker bash -c "apt-get update && apt-get install -y openjdk-11-jdk && apt-get clean && rm -rf /var/lib/apt/lists/*"

REM Set JAVA_HOME in spark-master
docker exec -u root spark-master bash -c "echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> /opt/bitnami/spark/conf/spark-env.sh"
docker exec -u root spark-master bash -c "echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /opt/bitnami/spark/conf/spark-env.sh"

REM Set JAVA_HOME in spark-worker
docker exec -u root spark-worker bash -c "echo 'export JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64' >> /opt/bitnami/spark/conf/spark-env.sh"
docker exec -u root spark-worker bash -c "echo 'export PATH=$JAVA_HOME/bin:$PATH' >> /opt/bitnami/spark/conf/spark-env.sh"

REM Copy requirements.txt to containers
echo Copying requirements.txt to spark-master...
docker cp requirements-spark.txt spark-master:/opt/bitnami/spark/requirements.txt
echo Copying requirements.txt to spark-worker...
docker cp requirements-spark.txt spark-worker:/opt/bitnami/spark/requirements.txt

REM Install dependencies in the spark-master container
echo Installing dependencies in spark-master container...
docker exec -it spark-master pip install -r /opt/bitnami/spark/requirements.txt

REM Install dependencies in the spark-worker container
echo Installing dependencies in spark-worker container...
docker exec -it spark-worker pip install -r /opt/bitnami/spark/requirements.txt

REM Check if installation was successful
if %errorlevel% neq 0 (
    echo Error installing dependencies.
    exit /b %errorlevel%
)

echo Dependencies and Java installed successfully.

REM Restart Spark containers
echo Restarting Spark containers...
docker restart spark-master
docker restart spark-worker

echo Installation completed successfully.
pause