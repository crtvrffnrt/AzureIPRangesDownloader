# AzureIPRangesDownloader

## Overview
### azure_ip_ranges_downloader.py is a Python script designed to fetch the latest IP ranges from Microsoft's Azure services and save them to a local JSON file. This script ensures that the latest IP ranges are always available by downloading and overwriting the existing file.

Sourcefile: [Azure IP Ranges](https://www.microsoft.com/en-us/download/details.aspx?id=53602 "Download Azure IP Ranges CSV")

### microsoft_ip_ranges_downloader.py is a Python script designed for the same purpose for Microsoft IP`s.

Sourcefile: **[Azure IP Ranges](https://www.microsoft.com/en-us/download/details.aspx?id=53602)**




## Features
- Fetches the latest IP ranges from Microsoft Azure.
- Saves the IP ranges to a JSON file.
- Overwrites the existing JSON file to ensure data is up-to-date.
- Runs silently without any console output or warnings.

## Prerequisites
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Usage
1. **Clone the repository:**
   ```
   git clone https://github.com/crtvrffnrt/AzureIPRangesDownloader.git
   cd AzureIPRangesDownloader
   pip install -r requirements.txt
   python azure_ip_ranges_downloader.py
   python microsoft_ip_ranges_downloader.py

   ``` 
