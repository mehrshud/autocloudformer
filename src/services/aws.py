from src.models import User, Resource
from src.config import Config
import boto3
import logging

logger = logging.getLogger(__name__)

class AWSService:
    def __init__(self, config: Config):
        self.config = config
        self.ec2 = boto3.client('ec2')

    def get_instances(self, user: User) -> list[Resource]:
        try:
            response = self.ec2.describe_instances()
            resources = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    resource = Resource(id=instance['InstanceId'], type='EC2', usage=instance['InstanceType'])
                    resources.append(resource)
            logger.info(f'Retrieved {len(resources)} EC2 instances for user {user.id}')
            return resources
        except Exception as e:
            logger.error(f'Error retrieving EC2 instances: {str(e)}')
            return []

    def scale_instance(self, resource: Resource, user: User) -> bool:
        try:
            self.ec2.modify_instance_attribute(InstanceId=resource.id, Attribute='InstanceType', Value='t2.micro')
            logger.info(f'Scaled EC2 instance {resource.id} for user {user.id}')
            return True
        except Exception as e:
            logger.error(f'Error scaling EC2 instance: {str(e)}')
            return False