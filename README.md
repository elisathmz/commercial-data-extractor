# Commercial Data Extractor (ETL)

A Python ETL pipeline that scrapes product listings from e-commerce pages, cleans and normalizes fields such as product titles and prices, and stores the structured data in a local SQLite database.

## Overview

This project automates the collection of product listing data from e-commerce pages. It extracts fields such as product titles and prices, cleans and normalizes the raw text, and loads the structured results into a local SQLite database for querying and further analysis.

## Tech Stack
- Python 3
- BeautifulSoup4 (HTML parsing)
- Pandas (Data manipulation and cleaning)
- SQLite & SQLAlchemy (Database operations)

## How it Works
The script connects to the target e-commerce page and parses the DOM to extract product titles and prices. Pandas is then used to clean and normalize the raw data, and SQLAlchemy loads the resulting DataFrame into a local SQLite table.