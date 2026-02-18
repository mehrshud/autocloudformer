from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

from src.models import User, Resource
from src.config import Config

logger = logging.getLogger(__name__)

class Database:
    """Class to handle database connections."""
    
    def __init__(self, config: Config):
        """
        Initialize the database connection.
        
        Args:
        config (Config): Configuration object containing the database URL.
        """
        self.config = config
        self.engine = None
        self.Session = None
        self.connect()

    def connect(self) -> None:
        """
        Establish a connection to the database.
        
        Raises:
        SQLAlchemyError: If the database connection fails.
        """
        try:
            self.engine = create_engine(self.config.db_url)
            self.Session = sessionmaker(bind=self.engine)
            logger.info("Database connection established.")
        except SQLAlchemyError as e:
            logger.error(f"Failed to connect to the database: {e}")
            raise e

    def get_session(self) -> Optional[sessionmaker]:
        """
        Get a database session.
        
        Returns:
        Optional[sessionmaker]: A database session if the connection is active, otherwise None.
        """
        if self.Session:
            return self.Session()
        else:
            logger.error("Database connection is not active.")
            return None

    def create_tables(self) -> None:
        """
        Create the database tables if they do not exist.
        
        Raises:
        SQLAlchemyError: If the table creation fails.
        """
        try:
            User.__table__.create(self.engine, checkfirst=True)
            Resource.__table__.create(self.engine, checkfirst=True)
            logger.info("Database tables created.")
        except SQLAlchemyError as e:
            logger.error(f"Failed to create database tables: {e}")
            raise e

db = Database(Config())