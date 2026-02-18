from src.models import User
from src.config import Config
from typing import List
import logging

logger = logging.getLogger(__name__)

def get_user_resources(user: User, config: Config) -> List[User]:
    """
    Retrieves resources for a given user.

    Args:
        user (User): The user object.
        config (Config): The configuration object.

    Returns:
        List[User]: A list of users with resources.
    """
    try:
        user_resources = []
        
        if user:
            logger.info(f"User ID: {user.id}")
            
            if config:
                logger.info(f"Configuration Debug Mode: {config.debug}")
                user_resources.append(user)
        
        return user_resources
    
    except Exception as e:
        logger.error(f"Error retrieving user resources: {str(e)}")
        return []

def calculate_resource_usage(resources: List[User]) -> float:
    """
    Calculates the total resource usage.

    Args:
        resources (List[User]): A list of users with resources.

    Returns:
        float: The total resource usage.
    """
    try:
        total_usage = 0.0
        
        for resource in resources:
            if hasattr(resource, 'usage'):
                total_usage += resource.usage
        
        return total_usage
    
    except Exception as e:
        logger.error(f"Error calculating resource usage: {str(e)}")
        return 0.0

def validate_config(config: Config) -> bool:
    """
    Validates the configuration.

    Args:
        config (Config): The configuration object.

    Returns:
        bool: True if the configuration is valid, False otherwise.
    """
    try:
        if hasattr(config, 'debug') and hasattr(config, 'db_url'):
            return True
        
        return False
    
    except Exception as e:
        logger.error(f"Error validating configuration: {str(e)}")
        return False