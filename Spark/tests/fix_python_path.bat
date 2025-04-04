@echo off
echo Fixing Python paths in spark-master...

REM Remove all Python symlinks
docker exec -u root spark-master bash -c "rm -f /usr/bin/python* /usr/bin/pip* /usr/local/bin/python* /usr/local/bin/pip*"

REM Create new symlinks to Python 3.12
docker exec -u root spark-master bash -c "ln -sf /usr/local/bin/python3.12 /usr/bin/python3 && ln -sf /usr/local/bin/python3.12 /usr/bin/python && ln -sf /usr/local/bin/pip3.12 /usr/bin/pip3 && ln -sf /usr/local/bin/pip3.12 /usr/bin/pip"

REM Update Spark environment configuration
docker exec -u root spark-master bash -c "echo 'export PYSPARK_PYTHON=/usr/bin/python3' > /opt/bitnami/spark/conf/spark-env.sh && echo 'export PYSPARK_DRIVER_PYTHON=/usr/bin/python3' >> /opt/bitnami/spark/conf/spark-env.sh"

REM Verify Python version
echo Verifying Python configuration...
docker exec spark-master python3 --version
docker exec spark-master pip3 --version

echo Done.
pause