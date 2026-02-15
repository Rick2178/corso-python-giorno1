import requests
import json
from datetime import datetime


class APIClient:
    """
    Un client per fare richieste HTTP a API esterne.
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({
            "User-Agent": "PythonDeveloper/1.0"
        })

    def get(self, endpoint, params=None):
        """
        Effettua una richiesta GET.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"errore": f"Richiesta fallita: {str(e)}"}

    def post(self, endpoint, data=None):
        """
        Effettua una richiesta POST.
        """
        try:
            url = f"{self.base_url}/{endpoint}"
            response = self.session.post(
                url,
                json=data,
                timeout=10,
                headers={"Content-Type": "application/json"}
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"errore": f"Richiesta fallita: {str(e)}"}
