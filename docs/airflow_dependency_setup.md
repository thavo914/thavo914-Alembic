# Airflow Dependency Management

## Automated Installation Setup


### 1. Create Entrypoint Script
Create `airflow/scripts/entrypoint.sh`:
```bash
#!/bin/bash
pip install -r /opt/airflow/requirements.txt
exec "$@"

2. Modify docker-compose.yml:
```yaml
```
  airflow-webserver:
    # ... existing config ...
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - ./Spark/Scripts:/opt/spark/scripts
      - ./airflow/config:/opt/airflow/config
      - ./requirements-airflow.txt:/opt/airflow/requirements.txt
      - ./airflow/scripts/entrypoint.sh:/entrypoint.sh
    entrypoint: ["/bin/bash", "/entrypoint.sh"]
    command: webserver

  airflow-scheduler:
    # ... existing config ...
    volumes:
      - ./airflow/dags:/opt/airflow/dags
      - ./Spark/Scripts:/opt/spark/scripts
      - ./airflow/config:/opt/airflow/config
      - ./requirements-airflow.txt:/opt/airflow/requirements.txt
      - ./airflow/scripts/entrypoint.sh:/entrypoint.sh
    entrypoint: ["/bin/bash", "/entrypoint.sh"]
    command: scheduler