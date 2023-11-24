FROM public.ecr.aws/lambda/python:3.9

# Copy requirements.txt
COPY requirements.txt ${LAMBDA_TASK_ROOT}

# Install the specified packages
RUN yum install -y java-1.8.0-openjdk
ENV JAVA_HOME /usr/lib/jvm/jre-1.8.0-openjdk
ENV PATH "$PATH:$JAVA_HOME/bin"
RUN pip install -r requirements.txt

# Copy function code
COPY sms_messages_as_spam_or_ham/src/model_manager.py ${LAMBDA_TASK_ROOT}
COPY src/post.py ${LAMBDA_TASK_ROOT}
COPY sms_messages_as_spam_or_ham/model/GBM_3_AutoML_1_20231123_10521 ${LAMBDA_TASK_ROOT}


# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "post.lambda_handler" ]