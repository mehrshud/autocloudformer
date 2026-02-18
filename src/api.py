from src.models import User
from src.config import Config
import logging
from typing import List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class API:
    """
    API endpoint definitions for the AutoCloudFormer system.

    Attributes:
        config (Config): Configuration object.
    """
    def __init__(self, config: Config):
        self.config = config

    def get_users(self) -> List[User]:
        """
        Retrieves a list of users from the database.

        Returns:
            List[User]: A list of user objects.
        """
        try:
            # Implement database query to retrieve users
            users = [User(id=1, name="John Doe", email="john@example.com")]
            logger.info("Successfully retrieved users")
            return users
        except Exception as e:
            logger.error(f"Error retrieving users: {e}", exc_info=True)
            raise

    def create_user(self, user: User) -> User:
        """
        Creates a new user in the database.

        Args:
            user (User): The user object to create.

        Returns:
            User: The created user object.
        """
        try:
            user.id = 2
            logger.info(f"Successfully created user {user.name}")
            return user
        except Exception as e:
            logger.error(f"Error creating user: {e}", exc_info=True)
            raise

    def get_resources(self) -> List[dict]:
        """
        Retrieves a list of resources from the database.

        Returns:
            List[dict]: A list of resource dictionaries.
        """
        try:
            resources = [{"id": 1, "type": "CPU", "usage": 0.5}]
            logger.info("Successfully retrieved resources")
            return resources
        except Exception as e:
            logger.error(f"Error retrieving resources: {e}", exc_info=True)
            raise

def main():
    config = Config(debug=True, db_url="localhost:5432")
    api = API(config)
    users = api.get_users()
    user = api.create_user(User(id=0, name="Jane Doe", email="jane@example.com"))
    resources = api.get_resources()

if __name__ == "__main__":
    main()