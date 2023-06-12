import os
import boto3

msg_interval_sec = 0.5

def get_sns_env_vars():
    topic_arn = os.environ["sns_topic_arn"]
    sns_region = os.environ["sns_topic_region"]
    return (topic_arn, sns_region)


def get_sqs_env_vars():
    queue_url = os.environ["sqs_queue_url"]
    sqs_region = os.environ["sqs_topic_region"]
    return (queue_url, sqs_region)


def get_cred_env_vars():
    access_key = os.environ["aws_access_key"]
    secret_key = os.environ["aws_secret_key"]
    return (access_key, secret_key)


def publish_message_to_sns(message: str):
    topic_arn, sns_region = get_sns_env_vars()
    access_key, secret_key = get_cred_env_vars()
    sns_client = boto3.client(
        "sns",
        region_name=sns_region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    message_id = sns_client.publish(
        TopicArn=topic_arn,
        Message=(
            message
        )
    )
    return message_id


def read_from_sqs_queue():
    queue_url, sqs_region = get_sqs_env_vars()
    access_key, secret_key = get_cred_env_vars()
    sqs_client = boto3.client(
        "sqs",
        region_name=sqs_region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
    )
    messages = sqs_client.receive_message(
        QueueUrl=queue_url,
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
    )
    return messages
