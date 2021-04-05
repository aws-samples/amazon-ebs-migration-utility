
import boto3
import random

NUM_OF_VOLS=5

# ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2', region_name='us-east-1')

east1_az_list=['us-east-1a', 'us-east-1b', 'us-east-1c', 'us-east-1d', 'us-east-1e', 'us-east-1f']
# east2_az_list=['us-east-2a', 'us-east-2b', 'us-east-2c']


for i in range(NUM_OF_VOLS):

    response = ec2_client.create_volume(
        AvailabilityZone=random.choice(east1_az_list),
        Size=1,
        
    
        VolumeType='gp2'
    )