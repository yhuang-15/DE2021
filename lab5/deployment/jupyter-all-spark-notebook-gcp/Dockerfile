FROM jupyter/all-spark-notebook:spark-3.1.1
USER root
RUN echo 'spark.jars.packages com.google.cloud.spark:spark-bigquery-with-dependencies_2.12:0.22.0' >> "${SPARK_HOME}/conf/spark-defaults.conf"

ENV PATH="/usr/lib/jvm/java-11-openjdk-amd64:$PATH"