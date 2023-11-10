# Web Crawler with Robots.txt and Sitemap Checking

## Overview
This Python script is a web crawler that searches the web using the Google Custom Search JSON API, checks each website's `robots.txt` for scraping permissions, and identifies if a `sitemap.xml` is present. The crawler stores the results in a CSV file, categorizing URLs as allowed or not allowed for scraping, and noting the presence of a sitemap.

## Features
- Google Custom Search JSON API Integration
- `robots.txt` Compliance Checking
- `sitemap.xml` Detection
- Results stored in CSV format
- Rate Limiting to prevent server overload
- Basic Error Handling and Logging

## Prerequisites
- Python 3
- `requests` and `google-api-python-client` libraries
- Access to Google Custom Search JSON API

## Installation
To install the necessary Python libraries, run:
pip install requests google-api-python-client

## Google Custom Search JSON API Setup

### Setting Up Google Custom Search Engine (CSE)
1. Visit the [Google Custom Search Engine](https://cse.google.com/cse/) page and sign in with your Google account.
2. Click on "Add" to create a new search engine.
3. Enter the sites you want to search across or leave it blank to search the entire web.
4. Click "Create" to get your Custom Search Engine ID.

### Getting Google API Key
1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project or select an existing one.
3. Navigate to “APIs & Services” > “Credentials”.
4. Click on “Create Credentials” and select “API key”. Your new API key will be displayed; copy it for later use.
5. Go to “Library”, search for “Custom Search API”, and enable it for your project.

### Implementing the API in the Script
Replace the placeholder `google_search` function with your implementation using the Google API key and Custom Search Engine ID.


## Configuration
Before running the script, ensure you have:
- Set up Google Custom Search JSON API and obtained an API key.
- Replaced the placeholder `google_search` function with an actual implementation using the Google API.
- Configured the `User-Agent` string in the script to represent your crawler accurately.

## Usage
Run the script in a Python environment:

python web_crawler.py

Enter your search query when prompted. The script will perform the search, check each URL, and save the results to `urls.csv`.

## Output
The script generates a CSV file (`urls.csv`) with the following columns:
- `URL`: The webpage URL
- `Allowed to Scrape`: Indicates if scraping is allowed as per `robots.txt`
- `Has Sitemap`: Indicates the presence of a `sitemap.xml`

## Contributing
Contributions to improve this script are welcome. Please follow the standard GitHub pull request process.

