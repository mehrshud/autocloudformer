from typing import List
from .models import User, Resource
from .config import Config
import logging
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam

class MachineLearningModel:
    """
    AutoCloudFormer machine learning model.

    Attributes:
    config (Config): System configuration.
    model (tensorflow.keras.Model): Compiled machine learning model.
    """

    def __init__(self, config: Config):
        """
        Initialize the machine learning model.

        Args:
        config (Config): System configuration.
        """
        self.config = config
        self.model = self.compile_model()

    def compile_model(self) -> Sequential:
        """
        Compile the machine learning model.

        Returns:
        tensorflow.keras.Model: Compiled machine learning model.
        """
        try:
            model = Sequential([
                Dense(64, activation='relu', input_shape=(1,)),
                Dense(1)
            ])
            model.compile(optimizer=Adam(), loss='mean_squared_error')
            return model
        except Exception as e:
            logging.error(f"Error compiling model: {e}", exc_info=True)
            raise

    def train(self, users: List[User], resources: List[Resource]) -> None:
        """
        Train the machine learning model.

        Args:
        users (List[User]): List of users.
        resources (List[Resource]): List of resources.
        """
        try:
            # Prepare data
            X = np.array([resource.usage for resource in resources])
            y = np.array([user.id for user in users])
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

            # Train model
            self.model.fit(X_train, y_train, epochs=10, batch_size=32, verbose=0)
        except Exception as e:
            logging.error(f"Error training model: {e}", exc_info=True)
            raise

    def predict(self, resource: Resource) -> int:
        """
        Make a prediction using the machine learning model.

        Args:
        resource (Resource): Resource to predict for.

        Returns:
        int: Predicted user ID.
        """
        try:
            return int(self.model.predict(np.array([[resource.usage]]))[0][0])
        except Exception as e:
            logging.error(f"Error making prediction: {e}", exc_info=True)
            raise