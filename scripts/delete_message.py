import boto3

# Initialize SQS client
sqs = boto3.client('sqs')
queue_url = 'https://sqs.<region>.amazonaws.com/<account_id>/YourQueueName'

receipt_handle = '<REPLACE_WITH_RECEIPT_HANDLE>'

sqs.delete_message(
    QueueUrl=queue_url,
    ReceiptHandle=receipt_handle
)

print("Message deleted successfully!")
