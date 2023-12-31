# sns-sqs-demo
Using SQS and SNS to communicate between two mock microservices.

To run the test functions, use:
```bash
pytest -s tests.py
```

To run the publisher-subscriber code, first create an SNS topic and an SQS queue using the AWS console. Subscribe your SQS queue to the SNS topic. Then set the following environmental variables based on your SNS and SQS deployments:
| Var                | Example   |
| :---               |    ----:  |  
| sns_topic_arn      | ...       | 
| sns_topic_region   | eu-west-3 | 
| sqs_queue_url      | ...       | 
| sqs_topic_region   | eu-west-3 | 
| aws_access_key     | AKIAIOSFODNN7EXAMPLE       |
| aws_secret_key     | wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY       |

Then you can run both as follows:
```bash
python3 publisher.py
python3 subscriber.py
```

Ideally, the AWS configurations are automated using a tool like Terraform.
