from src.models import User
from src.database import db
import logging
from googleapiclient.discovery import build
from google.oauth2 import service_account

class GCPService:
    def __init__(self, credentials_path: str):
        self.credentials_path = credentials_path
        self.credentials = service_account.Credentials.from_service_account_file(
            self.credentials_path, scopes=['https://www.googleapis.com/auth/cloud-platform']
        )
        self.gcp_client = build('cloudresourcemanager', 'v1', credentials=self.credentials)

    def get_gcp_resources(self, user: User) -> list:
        try:
            logging.info(f'Getting GCP resources for user {user.id}')
            projects = self.gcp_client.projects().list().execute()
            return projects.get('projects', [])
        except Exception as e:
            logging.error(f'Error getting GCP resources: {e}')
            return []

    def create_gcp_resource(self, user: User, resource_type: str) -> dict:
        try:
            logging.info(f'Creating GCP resource of type {resource_type} for user {user.id}')
            project = self.gcp_client.projects().create(body={'name': f'{user.name}-{resource_type}'}).execute()
            return project
        except Exception as e:
            logging.error(f'Error creating GCP resource: {e}')
            return {}