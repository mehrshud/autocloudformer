from src.config import Config
from typing import Optional
import logging

class User:
    """
    User model.

    Attributes:
        id (int): Unique identifier for the user.
        name (str): Name of the user.
        email (str): Email address of the user.
    """

    def __init__(self, id: int, name: str, email: str):
        """
        Initializes a new User instance.

        Args:
            id (int): Unique identifier for the user.
            name (str): Name of the user.
            email (str): Email address of the user.
        """
        self.id = id
        self.name = name
        self.email = email

    @staticmethod
    def get_user_by_id(id: int) -> Optional['User']:
        """
        Retrieves a user by their ID.

        Args:
            id (int): Unique identifier for the user.

        Returns:
            Optional[User]: The user instance if found, otherwise None.
        """
        try:
            # Simulating database query for demonstration purposes
            # In a real application, you would query your database here
            users = [User(1, 'John Doe', 'john@example.com'), User(2, 'Jane Doe', 'jane@example.com')]
            for user in users:
                if user.id == id:
                    return user
            return None
        except Exception as e:
            logging.error(f"Error retrieving user by ID: {e}", exc_info=True)
            return None