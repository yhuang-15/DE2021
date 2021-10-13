FROM bitnami/jupyterhub:1.4.2

RUN apt-get update -y && \
    apt-get install openjdk-11-jdk && \
    pip3 install --upgrade pip && \
    pip3 install pyspark==3.1.2

ENV PATH="/usr/lib/jvm/java-11-openjdk-amd64:$PATH"

CMD ["start-notebook.sh", "--NotebookApp.iopub_data_rate_limit=1000000000"]