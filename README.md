
## GuardDuty findings to Elastic/OpenSearch
#### This repository is an example on using EventBridge and Lambda functions to send the findings

## 1. Setup lambda function

#### 1.2 Install dependencies into the 'package' folder
```python
pip3 install -r requirements.txt --target package
```

#### Create zip file for upload in aws lambda service
```sh
cd package
zip -r ../lambda.zip *
cd ..
zip -g lambda.zip main.py
```

#### 1.2 Go to the interface and upload the zip file

#### 1.3 Ensure the "Handler" parameter in the interface is set to `main.handler`

#### 1.4 Add the env variables in the configuration tab
```
ES_HOST: https://<host-url>:<port>
ES_USERNAME: elasticsearch or opensearch password
ES_PASSWORD: elasticsearch or opensearch password 
INDEX_NAME: the name of the index where the logs are being saved
```

## 2. Setup EventBridge rule
Setup an EventBridge rule for the GuardDuty findings event to run the lambda function above.

#### Additional resources:
* https://docs.aws.amazon.com/lambda/latest/dg/python-package.html
* https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html
