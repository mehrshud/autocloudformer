from typing import Optional
import logging
import os

class Config:
    """
    Configuration class to store application settings.

    Attributes:
        debug (bool): Debug mode flag.
        db_url (str): Database connection URL.
    """
    def __init__(self, debug: bool, db_url: str):
        self.debug = debug
        self.db_url = db_url

    def get_debug_mode(self) -> bool:
        """
        Returns the debug mode flag.

        Returns:
            bool: Debug mode flag.
        """
        return self.debug

    def get_db_url(self) -> str:
        """
        Returns the database connection URL.

        Returns:
            str: Database connection URL.
        """
        return self.db_url

def load_config(debug: Optional[bool] = False, db_url: Optional[str] = None) -> Config:
    """
    Loads configuration from provided parameters or environment variables.

    Args:
        debug (bool, optional): Debug mode flag. Defaults to False.
        db_url (str, optional): Database connection URL. Defaults to None.

    Returns:
        Config: Loaded configuration instance.

    Raises:
        ValueError: If db_url is not provided and the environment variable is not set.
    """
    try:
        if not db_url:
            db_url = os.getenv("DB_URL")
            if not db_url:
                raise ValueError("Database URL is required")
        return Config(debug, db_url)
    except Exception as e:
        logging.error(f"Failed to load configuration: {e}")
        raise

def get_config() -> Config:
    """
    Returns the loaded configuration instance.

    Returns:
        Config: Loaded configuration instance.

    Raises:
        RuntimeError: If configuration is not loaded.
    """
    try:
        return load_config(debug=True, db_url=os.getenv("DB_URL", "mongodb://localhost:27017/"))
    except Exception as e:
        logging.error(f"Failed to retrieve configuration: {e}")
        raise RuntimeError("Configuration is not loaded")