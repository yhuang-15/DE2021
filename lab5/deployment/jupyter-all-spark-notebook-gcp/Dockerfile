FROM jupyter/all-spark-notebook:spark-3.1.1
USER root
# add bigquery dependecies
RUN echo 'spark.jars.packages com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.22.0,com.google.cloud.bigdataoss:gcs-connector:hadoop3-2.2.0' >> "${SPARK_HOME}/conf/spark-defaults.conf"
# Update the guava library needed by gcs connector
RUN mv ${SPARK_HOME}/guava-14.0.1.jar ${SPARK_HOME}/guava-14.0.1.jar.bk
RUN curl https://repo1.maven.org/maven2/com/google/guava/guava/30.1-jre/guava-30.1-jre.jar --output ${SPARK_HOME}/jars
