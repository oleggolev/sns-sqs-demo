import time
from lib import publish_message_to_sns, msg_interval_sec

# publishes a numbered message to the
# SNS topic every `msg_interval_sec` seconds
msg_sn = 0
while True:
    time.sleep(msg_interval_sec)
    ts_now = round(time.time() * 1000)
    msg = "{}: Message #{}".format(ts_now, msg_sn)
    sns_msg_id = publish_message_to_sns(msg)
    print("{} successfully published (SN #{})".format(sns_msg_id, msg_sn))
    msg_sn += 1