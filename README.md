# BookScraper

BookScraper is a Scrapy project designed to scrape data from the `bookstoscrape.com` website using Scrapy, and save the collected data in JSON or CSV format.

## Table of Contents

- [Introduction](#introduction)
- [Project Structure](#project-structure)
- [Key Features](#KeyFeatures)
- [Dependencies](#Dependencies)
- [Installation](#Installation)
- [Usage](#usage)
- [Scrapy Components](#scrapy-components)
  - [Scrapy Items](#scrapy-items)
  - [Pipelines](#pipelines)
  - [Middlewares](#middlewares)
## Introduction

The purpose of this project is to scrape data related to books from the `bookstoscrape.com` website using Scrapy. The data is collected by crawling web pages using a spider and is saved in JSON or CSV format.

## Project Structure

The project has the following structure:

bookscraper/<br>
├── bookscraper/<br>
│ ├── spiders/<br>
│ │ ├── data_spider.py<br>
│ │ └── init.py<br>
│ ├── items.py<br>
│ ├── middlewares.py<br>
│ ├── pipelines.py<br>
│ ├── settings.py<br>
│ └── scrapy.cfg<br>
└── README.md<br>


## KeyFeatures

- Setting up a virtual environment (`venv`) for Python.
- Installing Scrapy for web scraping.
- Crawling webpage data using a spider.
- Saving data to JSON or CSV files.
- Utilizing ScrapeOps for fake user agents.
- Implementing pipelines for data cleaning.

## Dependencies

To run this project, you need the following dependencies:

- Python 3.x
- Scrapy
- ScrapeOps API Key (for fake user agents)

## Installation

1. Clone this repository:

    ```bash
    git clone https://github.com/Govardhan211103/WebScraping.git
    cd bookscraper
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

3. Install the necessary packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Activate the virtual environment:

    ```bash
    venv\Scripts\activate
    ```
2. Get an API key form scrapeops.io :
 After getting an API key from scrapeops you can paste it in settings.py `SCRAPE_OPS_API_KEY`.
2. Run the spider to scrape data:

    ```bash
    scrapy crawl data_spider -o output.json  # Use -o output.csv for CSV output
    ```

    Replace `output.json` with your desired output file name.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvement, please open an issue or submit a pull request.

## Scrapy Components

### Scrapy Items

Scrapy Items are used to define the structure of the scraped data. They act as simple containers for the data you intend to scrape. Check the `items.py` file for item definitions specific to this project.

### Pipelines

Pipelines are where the scraped data is processed after being extracted by the spider. In this project, we implement pipelines for data cleaning.

### Middlewares

Middlewares in Scrapy are used to process requests and responses globally. In this project, we utilize `middlewares.py` to incorporate fake user agents from ScrapeOps using an API key.


---

Please ensure that you respect the terms of service of the website you are scraping and comply with all legal and ethical requirements.


"The Python Scrapy Playbook" is indeed a valuable resource for learning about web scraping with Scrapy.
If you are interested in learning more about web scraping and Scrapy, visiting https://thepythonscrapyplaybook.com/ can be a beneficial step to improve their understanding.
