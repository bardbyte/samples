import requests
from urllib.robotparser import RobotFileParser
from googleapiclient.discovery import build
import csv
import time
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = 'YOUR_API_KEY'
CSE_ID = 'YOUR_CSE_ID'


def check_sitemap(url):
    """
    Check if the given URL has a sitemap.xml file.
    """
    try:
        response = requests.get(url + '/sitemap.xml', timeout=10)
        return response.status_code == 200
    except requests.RequestException as e:
        logging.warning(f"Failed to fetch sitemap for {url}: {e}")
        return False

def is_allowed(url, user_agent='YourUserAgent'):
    """
    Check if the given URL allows web scraping for the specified user agent and check for sitemap.
    """
    rp = RobotFileParser()
    rp.set_url(url + '/robots.txt')
    try:
        rp.read()
        allowed = rp.can_fetch(user_agent, url)
    except Exception as e:
        logging.warning(f"Failed to parse robots.txt for {url}: {e}")
        allowed = False
    has_sitemap = check_sitemap(url)
    return allowed, has_sitemap


def google_search(query, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=query, cx=cse_id, **kwargs).execute()
    urls = [item['link'] for item in res['items']]
    return urls


def main():
    query = input("Enter your search query: ")
    urls = google_search(query)
    results = []

    for url in urls:
        time.sleep(1)  # Rate limiting
        allowed, has_sitemap = is_allowed(url)
        results.append([url, allowed, has_sitemap])

    with open('urls.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['URL', 'Allowed to Scrape', 'Has Sitemap'])
        writer.writerows(results)
    logging.info("Crawling completed. Results saved to urls.csv.")

if __name__ == "__main__":
    main()
