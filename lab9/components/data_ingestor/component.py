import argparse
import logging
import sys

from google.cloud import storage


def download_data(project_id, bucket, file_name, output_path):
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    client = storage.Client(project=project_id)
    bucket = client.get_bucket(bucket)
    blob = bucket.blob(file_name)
    blob.download_to_filename(output_path)
    logging.info('Downloaded Data!')


def parse_command_line_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--project_id', type=str, help="GCP project id")
    parser.add_argument('--bucket', type=str, help="Name of the data bucket")
    parser.add_argument('--file_name', type=str, help="Name of the training data set file name")
    parser.add_argument('--output_path', type=str, help="Name of the training data set file name")
    args = parser.parse_args()
    return vars(args)


if __name__ == '__main__':
    download_data(**parse_command_line_arguments())
