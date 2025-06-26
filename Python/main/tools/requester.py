import requests
from bs4 import BeautifulSoup
import os

class SimpleRequest:
    def __init__(self, base_url=None, headers=None):
        self.base_url = base_url
        self.headers = headers if headers is not None else {'User-Agent': 'Mozilla/5.0'}
    
    def _full_url(self, endpoint):
        if self.base_url:
            return f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        return endpoint


    def get(self, endpoint=None, params=None):
        url = self.base_url if endpoint in [None, ""] else self._full_url(endpoint)
        try:
            response = requests.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None


    def post(self, endpoint, data=None, json=None):
        url = self._full_url(endpoint)
        try:
            response = requests.post(url, headers=self.headers, data=data, json=json)
            response.raise_for_status()
            return response.text
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            return None

    def parse_html(self, html):
        return BeautifulSoup(html, 'html.parser')
    
    def download_pdf(self, url, save_path):
        try:
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            with open(save_path, 'wb') as file:
                file.write(response.content)
            #print(f"PDF uložené na: {save_path}")
        except requests.RequestException as e:
            print(f"Stiahnutie PDF zlyhalo: {e} :(")

# Príklad použitia
if __name__ == "__main__":
    req = SimpleRequest(base_url="https://example.com")

    # GET request
    html_content = req.get("/")
    if html_content:
        soup = req.parse_html(html_content)
        print(soup.title.text)  # Vypíše obsah <title> tagu

    # POST request
    data = {'key': 'value'}
    response = req.post("/submit", data=data)
    if response:
        soup = req.parse_html(response)
        print(soup.title.text)

    # Stiahnutie PDF
    req.download_pdf("files/sample.pdf", "sample.pdf")
