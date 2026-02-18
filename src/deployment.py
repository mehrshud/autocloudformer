from src.models import User
from src.config import Config
import boto3
import logging

logger = logging.getLogger(__name__)

class Deployment:
    def __init__(self, config: Config):
        """
        Initialize the deployment script with the given configuration.

        Args:
        config (Config): The configuration for the deployment.
        """
        self.config = config
        self.ec2 = boto3.client('ec2')

    def deploy(self, user: User) -> None:
        """
        Deploy the resources for the given user.

        Args:
        user (User): The user to deploy resources for.
        """
        try:
            # Create a new EC2 instance
            instance = self.ec2.run_instances(
                ImageId='ami-0c94855ba95c71c99',
                InstanceType='t2.micro',
                MinCount=1,
                MaxCount=1,
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [
                            {
                                'Key': 'User',
                                'Value': str(user.id)
                            }
                        ]
                    }
                ]
            )
            logger.info(f'Deployed instance {instance["Instances"][0]["InstanceId"]} for user {user.id}')
        except Exception as e:
            logger.error(f'Failed to deploy instance for user {user.id}: {str(e)}')
            raise

    def delete(self, user: User) -> None:
        """
        Delete the resources for the given user.

        Args:
        user (User): The user to delete resources for.
        """
        try:
            # Get the instances for the user
            instances = self.ec2.describe_instances(
                Filters=[{'Name': 'tag:User', 'Values': [str(user.id)]}]
            )['Reservations']
            # Terminate the instances
            for reservation in instances:
                for instance in reservation['Instances']:
                    self.ec2.terminate_instances(InstanceIds=[instance['InstanceId']])
            logger.info(f'Deleted instances for user {user.id}')
        except Exception as e:
            logger.error(f'Failed to delete instances for user {user.id}: {str(e)}')
            raise

def main() -> None:
    config = Config(debug=True, db_url='localhost:5432')
    deployment = Deployment(config)
    user = User(id=1, name='John Doe', email='john@example.com')
    deployment.deploy(user)
    deployment.delete(user)

if __name__ == '__main__':
    main()