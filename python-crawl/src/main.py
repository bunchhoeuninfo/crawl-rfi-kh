import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



# Function to crawl a webpage
def crawl_website(url, retries=3):

    session = requests.Session()
    
    session.headers.update = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    for attempt in range(retries):
        try:
            # Send a GET request to the URL
            response = session.get(url)

            # Check if the request was succesfully
            if response.status_code == 200:
                print(f"Succesfully access {url}")

                # Parse the HTML content using BeautifulSoup
                soup = BeautifulSoup(response.text, 'html.parser')

                # Example: Extract all links from the page
                links = soup.find_all('a')
                print(f"Found {len(links)} links on the page:")

                for link in links[:5]:
                    print(link.get('href'))
            else:
                print(f"Failed to access {url}. Status code: {response.status_code}")
        except Exception as e:
            print(f"An error occured: {e}")
    return None

# URL of the website to crawl
website_url = "https://www.rfi.fr/km/"

if __name__ == "__main__":
    crawl_website(website_url)