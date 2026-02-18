from dataclasses import dataclass
from logging import Logger, getLogger
from typing import Optional

class Resource:
    def __init__(self, id: int, type: str, usage: float):
        self.id = id
        self.type = type
        self.usage = usage

    def __str__(self) -> str:
        return f"Resource {self.id} ({self.type}): {self.usage}% usage"

    def to_dict(self) -> dict:
        return {"id": self.id, "type": self.type, "usage": self.usage}

def get_resource(id: int) -> Optional[Resource]:
    logger = getLogger(__name__)
    try:
        mock_db = {
            1: Resource(1, "EC2 instance", 50.0),
            2: Resource(2, "S3 bucket", 20.0),
        }
        return mock_db.get(id)
    except Exception as e:
        logger.error(f"Error retrieving resource: {e}", exc_info=True)
        return None

def create_resource(id: int, type: str, usage: float) -> Optional[Resource]:
    logger = getLogger(__name__)
    try:
        new_resource = Resource(id, type, usage)
        mock_db = {
            1: Resource(1, "EC2 instance", 50.0),
            2: Resource(2, "S3 bucket", 20.0),
        }
        mock_db[id] = new_resource
        return new_resource
    except Exception as e:
        logger.error(f"Error creating resource: {e}", exc_info=True)
        return None