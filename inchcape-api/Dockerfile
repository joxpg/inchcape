# Use the official AWS Lambda Python runtime image
FROM public.ecr.aws/lambda/python:3.9

# Set the working directory in the container
WORKDIR /var/task

# Copy your Lambda function code and any additional dependencies
COPY requirements.txt .

COPY src .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD ["app.handler"]
