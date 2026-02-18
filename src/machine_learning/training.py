from src.models import User, Resource
from src.config import Config
from src.database import db
import logging
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class MachineLearningTrainer:
    def __init__(self, config: Config):
        """
        Initialize the machine learning trainer.

        Args:
        config (Config): The application configuration.
        """
        self.config = config

    def fetch_data(self) -> list[Resource]:
        """
        Fetch data from the database.

        Returns:
        list[Resource]: A list of resource usage data.
        """
        try:
            return db.get_resources()
        except Exception as e:
            logger.error(f"Failed to fetch data: {e}")
            return []

    def split_data(self, data: list[Resource]) -> tuple[list[str], list[float], list[str], list[float]]:
        """
        Split the data into training and testing sets.

        Args:
        data (list[Resource]): The resource usage data.

        Returns:
        tuple[list[str], list[float], list[str], list[float]]: The training and testing data.
        """
        resources = [(resource.type, resource.usage) for resource in data]
        types = [resource[0] for resource in resources]
        usage = [resource[1] for resource in resources]
        return train_test_split(types, usage, test_size=0.2, random_state=42)

    def train_model(self, X_train: list[str], y_train: list[float]) -> tf.keras.Model:
        """
        Train a machine learning model.

        Args:
        X_train (list[str]): The training data input.
        y_train (list[float]): The training data output.

        Returns:
        tf.keras.Model: The trained machine learning model.
        """
        try:
            model = tf.keras.Sequential([tf.keras.layers.Dense(1)])
            model.compile(optimizer='adam', loss='mean_squared_error')
            model.fit(X_train, y_train, epochs=10, verbose=0)
            return model
        except Exception as e:
            logger.error(f"Failed to train model: {e}")
            return None

    def evaluate_model(self, model: tf.keras.Model, X_test: list[str], y_test: list[float]) -> float:
        """
        Evaluate the machine learning model.

        Args:
        model (tf.keras.Model): The trained machine learning model.
        X_test (list[str]): The testing data input.
        y_test (list[float]): The testing data output.

        Returns:
        float: The mean squared error of the model.
        """
        try:
            predictions = model.predict(X_test)
            return mean_squared_error(y_test, predictions)
        except Exception as e:
            logger.error(f"Failed to evaluate model: {e}")
            return 0.0

def main():
    config = Config(debug=True, db_url="localhost:5432")
    trainer = MachineLearningTrainer(config)
    data = trainer.fetch_data()
    X_train, X_test, y_train, y_test = trainer.split_data(data)
    model = trainer.train_model(X_train, y_train)
    if model:
        mse = trainer.evaluate_model(model, X_test, y_test)
        logger.info(f"Model MSE: {mse}")

if __name__ == "__main__":
    main()