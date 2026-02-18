from src.api import APIEndpoint
from src.models import User
from src.config import Config
from src.services.core import ServiceLayer
from src.machine_learning.model import MachineLearningModel
from src.database import db
import logging

def main() -> None:
    try:
        # Initialize logging
        logging.basicConfig(level=logging.INFO)
        
        # Load configuration
        config = Config(debug=True, db_url="postgresql://localhost:5432")
        
        # Initialize database connection
        db.init_app(app=None, url=config.db_url)
        
        # Create a test user
        user = User(id=1, name="John Doe", email="john@example.com")
        db.session.add(user)
        db.session.commit()
        
        # Create an API endpoint instance
        api_endpoint = APIEndpoint()
        
        # Create a service layer instance
        service_layer = ServiceLayer()
        
        # Create a machine learning model instance
        ml_model = MachineLearningModel()
        
        # Start the API server
        logging.info("Starting API server...")
        api_endpoint.start()
        
    except Exception as e:
        logging.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()