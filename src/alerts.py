from src.models import User
from src.config import Config
import logging

class AlertSystem:
    def __init__(self, config: Config) -> None:
        self.config = config
        self.logger = logging.getLogger(__name__)

    def send_alert(self, user: User, message: str) -> None:
        try:
            self.logger.info(f"Sending alert to user {user.id} with message: {message}")
            print(f"Alert sent to user {user.id}: {message}")
        except Exception as e:
            self.logger.error(f"Failed to send alert: {e}", exc_info=True)

    def notify_resource_usage(self, resource: 'Resource', user: User) -> None:
        try:
            message = f"Resource {resource.id} usage: {resource.usage}%"
            self.send_alert(user, message)
        except Exception as e:
            self.logger.error(f"Failed to notify resource usage: {e}", exc_info=True)