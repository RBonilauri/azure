import os
from azure.identity import DefaultAzureCredential
import config.config_file as config_file
import config.key_vault as key_vault
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, __version__
from azure.storage import *

class ADLServices:
    def __init__(self, credential=None, akv_service=None):
        if credential == None:
            credential = DefaultAzureCredential()
        if akv_service == None:
            akv_service = key_vault.AKVServices(credential=credential)

        adl_service = config_file.ADL_SERVICE
        key = akv_service.get_secret(config_file.AKV_ADL_SECRET_01)
        conn_string = f"https://{adl_service}.blob.core.windows.net/"
        self.blob_service_client = BlobServiceClient(conn_string, key)

    def get_all_pictures(self):
        #blob_content = self.blob_service_client.download_blob()
        #print(f"Your content is: '{blob_content}'")
        pictures = []
        container_client = self.blob_service_client.get_container_client(container="pictures")
        blob_list = container_client.list_blobs()
        for blob in blob_list:
            url = self.blob_service_client.get_blob_client(container="pictures", blob=blob.name).url
            pictures.append({"name": blob.name, "url": url})
        return pictures

    def insert_in_blob(self):
        blob = BlobClient.from_connection_string("my_connection_string", container="mycontainer", blob="my_blob")

        blob.upload_blob(data)
