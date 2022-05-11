import os
import boto3
import json
import requests
from requests.auth import HTTPBasicAuth
from requests import RequestException

# env variables
ES_HOST = os.environ['HOST']
ES_USERNAME = os.environ['USERNAME']
ES_PASSWORD = os.environ['PASSWORD']
INDEX_NAME = os.environ['INDEX_NAME']

# constants
DOC_TYPE = '_doc'
ES_URL = ES_HOST + '/' + INDEX_NAME + '/' + DOC_TYPE
ES_HEADERS = {'Content-Type': 'application/json'}
STATUS_OK = 'ok'
STATUS_CODE_OK = 201


# Lambda execution starts here
def handler(event, context):
    s3 = boto3.client('s3')

    document = event['detail']
    # Map field 'createdAt' to '@timestamp' for automatic identification from OpenSearch/Elasticsearch
    document['@timestamp'] = document['createdAt']

    r = requests.post(
        ES_URL,
        auth=HTTPBasicAuth(ES_USERNAME, ES_PASSWORD),
        json=document,
        headers=ES_HEADERS
    )

    if r.status_code == STATUS_CODE_OK:
        return STATUS_OK, r.status_code

    raise RequestException(r.json())
