FROM bitnami/jupyterhub:1.4.2
USER root
RUN apt-get update -y && \
    apt-get install openjdk-11-jdk

RUN pip3 install --upgrade pip && \
    pip3 install pyspark==3.1.2

USER 1001
ENV PATH="/usr/lib/jvm/java-11-openjdk-amd64:$PATH"