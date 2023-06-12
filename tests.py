import os
import json

import boto3
from moto import mock_sns, mock_sqs
from lib import read_from_sqs_queue, publish_message_to_sns

@mock_sns
def test_publish_message_to_sns():
    region = os.environ["sns_topic_region"]
    sns_resource = boto3.resource(
        "sns",
        region_name=region,
    )
    topic = sns_resource.create_topic(
        Name="test-topic"
    )
    os.environ["sns_topic_arn"] = topic.arn
    test_message = "test_message"
    message_id = publish_message_to_sns(test_message)

    assert message_id["ResponseMetadata"]["HTTPStatusCode"] == 200


@mock_sns
@mock_sqs
def test_read_from_sqs_queue():
    sns_region = os.environ["sns_topic_region"]
    sqs_region = os.environ["sqs_topic_region"]
    sns_resource = boto3.resource(
        "sns",
        region_name=sns_region
    )
    topic = sns_resource.create_topic(
        Name="test-topic"
    )
    sqs_resource = boto3.resource(
        "sqs",
        region_name=sqs_region,
    )
    queue = sqs_resource.create_queue(
        QueueName="test-queue",
    )
    os.environ["sqs_queue_url"] = queue.url
    os.environ["sns_topic_arn"] = topic.arn

    topic.subscribe(
        Protocol="sqs",
        Endpoint=queue.attributes["QueueArn"],
    )

    test_message = "test_message"
    message_id = publish_message_to_sns(test_message)

    messages = read_from_sqs_queue()
    message_body = json.loads(messages["Messages"][0]["Body"])

    assert message_body["MessageId"] == message_id["MessageId"]
    assert message_body["Message"] == test_message
