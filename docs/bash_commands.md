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

# Install requirements
docker exec -u root airflow-webserver pip install -r /opt/spark/requirements.txt