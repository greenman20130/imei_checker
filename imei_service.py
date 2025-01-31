import requests
import json
from config import API_TOKEN

class ImeiService:
    BASE_URL = 'https://api.imeicheck.net/'

    @staticmethod
    def check_imei(imei):
        
        headers = {
            'Authorization': f'Bearer {API_TOKEN}',
            'Accept-Language': 'en',
            }
        
        # Add body
        payload = {
            "deviceId": f"{imei}",
            "serviceId": 12
            }    
        
        # Execute request
        response = requests.request("POST", "https://api.imeicheck.net/v1/checks", headers=headers, data=payload)
        return response.json()