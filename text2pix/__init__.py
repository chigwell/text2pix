import requests
from urllib.parse import quote

BASE_URL = "https://wsrv.nl/?cx=0&cy=0&cw=1000&ch=720&fit=cover&a=focal&&url=https://image.pollinations.ai/prompt/"


def generate_image_from_text(text_description):
    encoded_text = quote(text_description)
    full_url = BASE_URL + encoded_text
    response = requests.get(full_url)

    if response.status_code == 200:
        return response.content
    else:
        raise Exception("Failed to retrieve the image.")
