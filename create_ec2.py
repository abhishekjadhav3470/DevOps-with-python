import boto3
import boto3.session

aws_management_console = boto3.session.Session(profile_name="admin")

ec2_console = aws_management_console.client('ec2')

response = ec2_console.run_instances(
    ImageId='ami-068e0f1a600cd311c',
    InstanceType='t2.micro',
    MaxCount=1,
    MinCount=1,
)
