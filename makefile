deploy:
	sam build
	sam validate
	sam deploy --stack-name spam-or-ham --template-file template.yaml --capabilities CAPABILITY_NAMED_IAM