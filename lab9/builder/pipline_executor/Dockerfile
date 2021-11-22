FROM python:3.7
ADD pipline_executor.py ./
ADD requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python","pipline_executor.py"]