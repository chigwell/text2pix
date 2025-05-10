import requests
from urllib.parse import quote

BASE_URL = "https://wsrv.nl/?cx=0&cy=0&cw=1000&ch=960&fit=cover&a=focal&&url=https://image.pollinations.ai/prompt/"

def generate_image_from_text(text_description):
    encoded_text = quote(text_description)
    full_url = BASE_URL + encoded_text
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(full_url, headers=headers, timeout=30)
        if response.status_code == 200:
            content_type = response.headers.get('content-type')
            if content_type and 'image' in content_type.lower():
                return response.content
            else:
                raise Exception(f"Failed to retrieve a valid image. Content-Type: {content_type}. Full response might indicate an error from the server.")
        else:
            raise Exception(f"Failed to retrieve the image. Status Code: {response.status_code}. Response: {response.text}")

    except requests.exceptions.RequestException as e:
        raise Exception(f"Request failed: {e}")