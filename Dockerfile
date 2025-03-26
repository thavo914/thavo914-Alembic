FROM openjdk:8-jdk-alpine

# Install necessary dependencies
RUN apk add --no-cache \
    bash \
    wget \
    curl \
    python3 \
    py3-pip \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    openssl-dev

# Set Spark version and download URL
ENV SPARK_VERSION=3.2.4
ENV HADOOP_VERSION=3.2

# First upgrade pip and install required Python packages
RUN pip3 install --upgrade pip && \
    pip3 install --no-cache-dir \
    pyspark==${SPARK_VERSION} \
    apache-airflow==2.7.1 \
    pandas \
    numpy

# Download and install Spark
RUN wget https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -O /tmp/spark.tgz \
    && tar -xvzf /tmp/spark.tgz -C /opt/ \
    && mv /opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION} /opt/spark \
    && rm -f /tmp/spark.tgz

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin
ENV JAVA_HOME=/usr/lib/jvm/java-1.8-openjdk
ENV PYTHONPATH=$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.9.7-src.zip

# Create work directories
RUN mkdir -p /opt/spark-apps /opt/spark-data /opt/airflow

WORKDIR /opt/spark

EXPOSE 4040 7077 8080

# Set the entrypoint to start Spark
ENTRYPOINT ["/opt/spark/bin/spark-shell"]
