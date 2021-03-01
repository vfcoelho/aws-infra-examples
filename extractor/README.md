serverless deploy

pipenv lock --r > requirements.txt
pipenv run pip install -t vendored -r requirements.txt

COMMAND=$(aws ecr get-login --no-include-email --region us-west-2)
sudo $COMMAND
cluster_identifier = 'sls-examples-extractor-develop'
sudo docker build -t ${cluster_identifier} .
sudo docker tag ${cluster_identifier}:latest ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${cluster_identifier}:latest
sudo docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${AWS_DEFAULT_REGION}.amazonaws.com/${cluster_identifier}:latest