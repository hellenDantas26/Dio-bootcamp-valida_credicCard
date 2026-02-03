import os
from dotenv import load_dotenv

load_dotenv()

class Config:

    ENDPOINT = os.getenv("ENDPOINT")
    SUBSCRIPTION_KEY = os.getenv("SUBSCRIPTION_KEY")
    AZURE_STORE_CONNECTION_STRING = os.getenv("AZURE_STORE_CONNECTION_STRING")
    CONTAINER_NAME = os.getenv("CONTAINER_NAME")