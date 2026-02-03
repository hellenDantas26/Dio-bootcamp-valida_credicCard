import os
from azure.storage.blob import BlobServiceClient

import streamlit as st
from ultils.config import Config

def upload_file_to_blob(file, file_name):
    try:
        connect_str = Config.AZURE_STORE_CONNECTION_STRING
        container_name = Config.CONTAINER_NAME

        blob_service_client = BlobServiceClient.from_connection_string(Config.AZURE_STORE_CONNECTION_STRING)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        blob_client.upload_blob(file, overwrite=True)

        blob_url = f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{file_name}"
        return blob_url
    except Exception as e:
        st.error(f"Erro ao enviar o arquivo para o Azure Blob Storage: {e}")
        return None
    