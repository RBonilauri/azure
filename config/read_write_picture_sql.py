import time
from io import BytesIO
from PIL import Image
import matplotlib.pyplot as plt

import requests

import config.azure_config as azure_config
import config.python_code as image_analysis

az = azure_config.AzureServices()

computervision_client = az.computer_vision
pictures = az.get_all_pictures()


def description_insert_image(picture):
    url = picture.get('url')
    name = picture.get('name')

    print("url", url)
    print("name", name)
    features = ['Description', 'Tags']
    img = Image.open(BytesIO(requests.get(url).content))
    fig = plt.figure(figsize=(8, 8))
    plt.title(name)
    plt.axis('off')
    plt.imshow(img)
    plt.show()

    az.analyse_picture(name, url)



#for i in pictures:
#    description_insert_image(i)
#    time.sleep(5)