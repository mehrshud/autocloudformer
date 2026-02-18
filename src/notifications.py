from src.models import User
from src.config import Config
from src.database import db
import logging

class Notification:
    def __init__(self, user: User, message: str):
        """
        Initialize a notification for a user.

        Args:
        - user (User): The user to send the notification to.
        - message (str): The message to send in the notification.
        """
        self.user = user
        self.message = message

    def send(self) -> None:
        """
        Send the notification to the user.
        """
        try:
            # Log the notification being sent
            logging.info(f"Sending notification to user {self.user.id}: {self.message}")

            # Send the notification via email (for example)
            # Here we use a placeholder for the actual email sending logic
            # This could be replaced with an email library like smtplib
            print(f"Sending email to {self.user.email}: {self.message}")
        except Exception as e:
            # Log any errors that occur during notification sending
            logging.error(f"Error sending notification: {e}", exc_info=True)

def send_notification(user: User, message: str) -> None:
    """
    Send a notification to a user.

    Args:
    - user (User): The user to send the notification to.
    - message (str): The message to send in the notification.
    """
    notification = Notification(user, message)
    notification.send()

def notify_user_of_resource_usage(user: User, resource: 'Resource') -> None:
    """
    Notify a user of their resource usage.

    Args:
    - user (User): The user to notify.
    - resource (Resource): The resource to notify the user about.
    """
    message = f"Your {resource.type} usage is {resource.usage}%"
    send_notification(user, message)