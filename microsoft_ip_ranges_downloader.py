import requests
from bs4 import BeautifulSoup
import os

class AzureCSVDownloader:
    def __init__(self):
        self.azure_download_page = "https://www.microsoft.com/en-us/download/details.aspx?id=53602"
        self.headers = {
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'
        }

    def _get_direct_link(self):
        r = requests.get(self.azure_download_page, headers=self.headers)
        soup = BeautifulSoup(r.content, "html.parser")
        direct_link = soup.select_one(".dlcdetail__download-btn")["href"]
        return direct_link

    def download_and_save_csv(self, save_path="./MSFT_PublicIPs.csv"):
        direct_link = self._get_direct_link()
        r = requests.get(direct_link)
        with open(save_path, 'wb') as f:
            f.write(r.content)

if __name__ == "__main__":
    downloader = AzureCSVDownloader()
    downloader.download_and_save_csv()
