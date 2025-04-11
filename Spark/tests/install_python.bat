@echo off
echo Installing Python 3.12.3 and dependencies...

docker exec -it -u root spark-master bash -c "apt-get update && apt-get install -y wget gcc python3-dev build-essential software-properties-common libffi-dev && wget https://www.python.org/ftp/python/3.12.3/Python-3.12.3.tgz && tar -xf Python-3.12.3.tgz && cd Python-3.12.3 && ./configure --enable-optimizations --enable-loadable-sqlite-extensions --with-system-ffi && make -j $(nproc) && make install && cd .. && rm -rf Python-3.12.3* && rm -f /opt/bitnami/python/bin/python3 && rm -f /opt/bitnami/python/bin/pip3 && ln -sf /usr/local/bin/python3.12 /opt/bitnami/python/bin/python3 && ln -sf /usr/local/bin/pip3.12 /opt/bitnami/python/bin/pip3 && python3 -m ensurepip && pip3 install --upgrade pip"

echo.
echo Verifying Python installation...
docker exec -it spark-master /opt/bitnami/python/bin/python3 --version
docker exec -it spark-master python3 --version
docker exec -it airflow-webserver python3 --version

echo.
echo Verifying pip installation...
docker exec -it spark-master /opt/bitnami/python/bin/pip3 --version

echo.
echo Testing Python ctypes...
docker exec -it spark-master /opt/python/bin/python3 -c "import ctypes; print('ctypes available')"

echo.
echo Installation and verification complete.
pause