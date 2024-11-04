# Amazon SQS Demo Project

This project demonstrates the basics of using Amazon Simple Queue Service (SQS) to send, receive, and delete messages. SQS enables decoupling of components, making cloud applications more scalable and reliable.

## Features
- **Send Messages**: Send messages to an SQS queue.
- **Receive Messages**: Retrieve messages from the SQS queue.
- **Delete Messages**: Remove messages from the queue to prevent reprocessing.

## Getting Started

### Prerequisites
- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html)
- Python 3.x
- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) (AWS SDK for Python)

### Setup

1. **Configure AWS CLI**: 
   ```bash
   aws configure
   ```
   Enter your AWS Access Key, Secret Key, and region.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/sqs-demo.git
   cd sqs-demo
   ```

3. **Install Requirements**:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

#### Sending a Message
Use the `send_message.py` script to send a message to your SQS queue:
```bash
python scripts/send_message.py
```

#### Receiving a Message
Use the `receive_message.py` script to retrieve a message from your SQS queue:
```bash
python scripts/receive_message.py
```

#### Deleting a Message
Use the `delete_message.py` script to delete a received message from your SQS queue:
```bash
python scripts/delete_message.py
```
