FROM jupyter/base-notebook:hub-1.4.2

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev && \
    pip3 install --upgrade pip && \
    pip3 install wget==3.2 pyspark==3.1.2

RUN sudo apt-get install openjdk-11-jdk

ENV PATH="/usr/lib/jvm/java-11-openjdk-amd64:$PATH"

CMD ["start-notebook.sh", "--NotebookApp.iopub_data_rate_limit=1000000000"]