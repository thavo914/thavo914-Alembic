@echo off
echo Setting up directories...
docker exec -u root spark-master mkdir -p /tmp/logs /tmp/derby
docker exec -u root spark-master chmod 777 /tmp/logs /tmp/derby

echo Copying RDD.py to Spark container...
docker cp Spark\Scripts\RDD.py spark-master:/opt/bitnami/spark/scripts/

echo Running Spark script...
docker exec -it spark-master spark-submit /opt/bitnami/spark/scripts/RDD.py

echo.
echo Spark UI is available at: http://localhost:8080
echo Press any key to open the Spark UI in your default browser...
pause
start http://localhost:8080

pause