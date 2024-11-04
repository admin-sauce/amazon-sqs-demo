import boto3
import json

# Load example message from JSON
with open('example_message.json') as f:
    message_body = json.load(f)

# Initialize SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.<region>.amazonaws.com/<account_id>/YourQueueName'

# Send message
response = sqs.send_message(
    QueueUrl=queue_url,
    MessageBody=json.dumps(message_body)
)

print("Message sent! Message ID:", response['MessageId'])
