FROM openjdk:8-jdk-alpine

# Install necessary dependencies
RUN apk add --no-cache bash wget curl

# Set Spark version and download URL
ENV SPARK_VERSION=3.5.5
ENV HADOOP_VERSION=3.3

# Download and install Spark
RUN wget https://downloads.apache.org/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz -O /tmp/spark.tgz \
    && tar -xvzf /tmp/spark.tgz -C /opt/ \
    && rm -f /tmp/spark.tgz

# Set environment variables
ENV SPARK_HOME=/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}
ENV PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin

# Expose ports for Spark UI and driver
EXPOSE 4040 7077 8080

# Set the entrypoint to start Spark
ENTRYPOINT ["/opt/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}/bin/spark-shell"]
