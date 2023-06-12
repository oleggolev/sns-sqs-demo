import json
import time
from lib import read_from_sqs_queue, msg_interval_sec

# reads a numbered message to the
# SNS topic every `msg_interval_sec` seconds
time.sleep(msg_interval_sec * 2 / 1.5)
while True:
    time.sleep(msg_interval_sec)
    message = read_from_sqs_queue()
    if "Messages" in message:
        message_body = json.loads(message["Messages"][0]["Body"])["Message"]
        print("Successfully read: {}".format(message_body))
    else:
        print("Nothing in SQS queue")
