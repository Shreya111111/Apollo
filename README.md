

# Apollo.io Scraper API

## Introduction

The Apollo.io Scraper API is a web service designed to scrape search results from Apollo.io, a platform for sales and marketing intelligence. This API allows users to retrieve search results for a given name and organization name through two endpoints: `/scrape` and `/scrape_results`. The `/scrape` endpoint initiates the scraping process and returns a job ID, while the `/scrape_results` endpoint retrieves the status of the job and the scraped results once the job is finished.

## Tech Stack

- **FastAPI**: A modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **Requests**: A simple HTTP library for making requests and working with APIs.
- **Pydantic**: Data validation and settings management using Python type annotations.

## Installation Instructions

1. Clone the repository:

   ```bash
   git clone https://github.com/Shreya111111/Apollo
   cd Apollo
   ```

2. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
  
- **Testing**:
  - Unit tests for the API endpoints are written using Pytest and FastAPI's TestClient.
