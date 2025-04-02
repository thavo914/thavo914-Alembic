# Bash Commands Reference

## Docker Commands

### Container Management
```bash

# Start containers
docker-compose up -d

# Stop containers
docker-compose down

# Check container status
docker ps

# View container logs
docker logs container_name

# Copy files to Spark container
docker cp /path/to/file spark-master:/opt/spark/scripts/

# Execute Spark job
docker exec -it spark-master spark-submit /opt/spark/scripts/RDD.py

# Initialize database
docker exec airflow-webserver airflow db init

# Create admin user
docker exec airflow-webserver airflow users create \
    --username admin \
    --password admin \
    --firstname Admin \
    --lastname User \
    --role Admin \
    --email admin@example.com

# Copy Airflow requirements.txt to airflow-webserver
docker cp requirements-airflow.txt airflow-webserver:/opt/airflow/requirements.txt

# Set permissions and install Airflow requirements
docker exec -u root airflow-webserver chown -R airflow: /opt/airflow && \
docker exec -u root airflow-webserver pip install -r /opt/airflow/requirements.txt

# Copy Spark requirements.txt to spark-master
docker cp requirements-spark.txt spark-master:/opt/spark/requirements.txt

# Install Spark requirements
docker exec -u root spark-master pip install -r /opt/spark/requirements.txt

# Check Java version in containers
docker exec spark-master java -version
docker exec airflow-webserver java -version

# Test DAG execution - Runs a specific DAG for testing purposes
docker exec -it airflow-webserver bash -c "airflow dags test spark_etl_pipeline 2025-03-28"

docker exec -it airflow-webserver bash -c "airflow dags test spark_user_etl 2025-04-01"




