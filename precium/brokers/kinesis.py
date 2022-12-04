"""
Inspired by https://docs.aws.amazon.com/kinesisanalytics/latest/java/gs-python-createapp.html
"""

import boto3

boto3.client("kinesis", region_name="us-west-2")
