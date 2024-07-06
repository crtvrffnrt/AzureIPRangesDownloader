# AzureIPRangesDownloader

## Overview
AzureIPRangesDownloader is a Python script designed to fetch the latest IP ranges from Microsoft's Azure services and save them to a local JSON file. This script ensures that the latest IP ranges are always available by downloading and overwriting the existing file.

## Features
- Fetches the latest IP ranges from Microsoft Azure.
- Saves the IP ranges to a JSON file.
- Overwrites the existing JSON file to ensure data is up-to-date.
- Runs silently without any console output or warnings.

## Prerequisites
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/AzureIPRangesDownloader.git
   cd AzureIPRangesDownloader
   pip install -r requirements.txt
   python azure_ip_ranges_downloader.py
