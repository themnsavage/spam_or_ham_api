# spam_or_ham_api
Train a machine learning model and deploy it as a web service using cloud platforms or local deployment tools. Understand the complete process of transforming a data science model into a consumable API endpoint.

## expected input and output:
- input: a message
- output: the message you sent and if it is spam or ham

## challenges:
- AWS lambdas does not support machine learning python libraries like pandas by default. So I had to work around this by creating a dockerfile and then upload the docker image to AWS ecr. To allow the AWS lambda function to pull image and run using image.

## tools used for this project:
- AWS
- sam
- python
- autoML tool: h2o
- docker

## how to deploy:
- make sure you have aws cli and sam config
- run make command `make deploy`

## how to make prediction request to api:
- get api url from aws console
- use postman
- make `POST` request
- add to body with key message and value with message you want to make prediction on

## example of using api to predict if message is spam or ham:
![image](https://github.com/themnsavage/spam_or_ham_api/assets/60998598/1ecb2d1a-1b61-48f6-af16-071fb8eccce4)

