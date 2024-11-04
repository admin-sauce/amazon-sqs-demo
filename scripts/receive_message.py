import boto3
import json

# Initialize SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.<region>.amazonaws.com/<account_id>/YourQueueName'

# Receive message
response = sqs.receive_message(
    QueueUrl=queue_url,
    MaxNumberOfMessages=1,
    WaitTimeSeconds=5
)

if 'Messages' in response:
    message = response['Messages'][0]
    print("Received message:", json.loads(message['Body']))
else:
    print("No messages available.")
