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

# Final Project Report

## Introduction:
- Using the model from assignment 4 which would detect if message is spam or ham. I created an API with an endpoint where users can do a POST protocol to see if message is spam or ham.

## Dataset Selection & Model Training
-  The data set I used for my model contain one feature(message) and one label(spam or ham). With this data set I generated new features and split the data into two sets: training and testing. For training my model I use a python AutoML library h2o.

## Deployment Preparation:
- tools I used to create my api were AWS, sam, python, and docker. I chose AWS as the service to host my API. Which included an API gateway and a lambda function. I used sam to deploy my services to AWS to create my API. Python was the chosen language for the code in my lambda function and code for my ML model. Docker was used in this project to help containerize the code for both lambda and ML model.

## Deployment and Testing:
- For deploying my API I used the tool sam and a sam template file to help tell AWS(through cloudformation) what resources and services to create. I pushed the image from my docker file to AWS ECR using the AWS CLI.

- After deploying my API I then used a combination of the AWS console and postman to help test my API.

## Reflection:
-  One big challenge I ran into was that AWS lambda functions did not support some of python libraries like pandas. The solution I cam up with was using an docker image to containerize my code for the lambda to run on.

-  Another big problem I ran into was the lambda function had a long cold start time (how long it takes to run lambda function first time). Due to this I would time out the API request from postman, due to it having a max timeout of thirty seconds. Sadly AWS does not allow you to increase the timeout time. So one solution to this is having a number of lambda functions always running, I did not implement this solution, because this feature is not included in the AWS free tier. But it is fine because if you do multiple requests(one or two) it will successfully respond to the user.

## Conclusion
- In this project, I turned a spam detection model from a previous assignment into an API. Users can send messages through a POST request to check if they're spam or not. I used a dataset with message features and labels (spam or ham) and trained the model using the h2o AutoML library. The API was built using AWS, Python, Docker, and the SAM tool. Deploying it involved setting up AWS resources and testing with Postman. Challenges included dealing with unsupported Python libraries in AWS Lambda and the initial slow response of Lambda functions. While not perfect, the API works well after a few requests.

## Image of POST request to API using postman:
![image](https://github.com/themnsavage/spam_or_ham_api/assets/60998598/0a3538d4-c4d6-42e2-b6e3-8124ee285f6c)

## References:
- data set used: https://archive.ics.uci.edu/dataset/228/sms+spam+collection

