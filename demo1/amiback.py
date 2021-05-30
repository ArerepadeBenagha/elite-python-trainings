import boto3
import datetime

today = datetime.date.today()

session = boto3.Session(region_name="us-east-1")
ec2 = session.resource('ec2')

instances = ec2.instances.filter(
    Filters=[{'Name': 'tag:Backup', 'Values': ['Yes']}])


for instance in instances:
    instance_name = ''
    for tag in instance.tags:
        if tag["Key"] == 'Name':
            instance_name = tag["Value"]
    print(instance.id, "{0}-{1}".format(instance_name, today.strftime("%Y-%m-%d")))
    instance.create_image(
        Name="{0}-{1}".format(instance_name, today.strftime("%Y-%m-%d")),
        InstanceId=instance.id,
        Description='Quarterly-Backup-AMI',
        NoReboot=True,
        TagSpecifications=[
            {
                'ResourceType': 'snapshot',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': 'Testing123123'
                    },
                ]
            },
        ]
    )