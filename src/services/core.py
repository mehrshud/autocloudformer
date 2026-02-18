from src.models import User, Resource
from src.database import db
from sqlalchemy.exc import SQLAlchemyError

class CoreService:
    """
    This class provides core services for the AutoCloudFormer system.
    """
    
    def get_user(self, user_id: int) -> User:
        """
        Retrieves a user by ID.

        Args:
        user_id (int): The ID of the user to retrieve.

        Returns:
        User: The retrieved user.
        """
        try:
            user = db.session.query(User).filter_by(id=user_id).first()
            if user is None:
                raise ValueError(f"User with ID {user_id} not found")
            return user
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve user: {str(e)}")

    def get_resources(self) -> list:
        """
        Retrieves all resources.

        Returns:
        list: A list of resources.
        """
        try:
            resources = db.session.query(Resource).all()
            return resources
        except SQLAlchemyError as e:
            db.session.rollback()
            raise Exception(f"Failed to retrieve resources: {str(e)}")