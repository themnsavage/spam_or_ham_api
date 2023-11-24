deploy:
	sam build
	sam validate
	docker push 146748406015.dkr.ecr.us-east-1.amazonaws.com/spam-or-ham
	sam deploy --stack-name spam-or-ham --template-file template.yaml --capabilities CAPABILITY_NAMED_IAM --image-repository 146748406015.dkr.ecr.us-east-1.amazonaws.com/spam-or-ham