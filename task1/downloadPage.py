# Code generated using ChatGPT
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import os
import urllib

def download_page(url, download_folder):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Create a folder for the downloaded content
        os.makedirs(download_folder, exist_ok=True)
        
        # Download HTML source code
        html_filename = os.path.join(download_folder, 'index.html')
        with open(html_filename, 'w', encoding='utf-8') as html_file:
            html_file.write(response.text)
        
        # Download graphics
        for img_tag in soup.find_all('img'):
            img_url = img_tag.get('src')
            if img_url:
                img_url = urljoin(url, img_url)
                img_name = os.path.basename(urlparse(img_url).path)
                img_path = os.path.join(download_folder, img_name)
                urllib.request.urlretrieve(img_url, img_path)
                print(f'Downloaded: {img_path}')
        
        print(f'HTML source code downloaded: {html_filename}')
    else:
        print(f'Error: Unable to download page. Status code {response.status_code}')

# Example usage
url_to_download = 'https://www.vlr.gg/rankings'
download_folder = 'content'
download_page(url_to_download, download_folder)
