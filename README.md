# Commercial Data Extractor (ETL)

A straightforward Python script for Web Scraping and ETL (Extract, Transform, Load). It automates the extraction of commercial data, sanitizes the raw text, and stores it securely in a relational database.

## Overview
Manual data collection is slow and prone to errors. This project tackles that issue by automating the collection of product data (titles and prices) from e-commerce environments. It cleans the raw strings (handling currency symbols and formatting) and loads the structured data into a local SQLite database, making it ready for querying and analysis.

## Tech Stack
- Python 3
- BeautifulSoup4 (HTML parsing)
- Pandas (Data manipulation and cleaning)
- SQLite & SQLAlchemy (Database operations)

## How it Works
The script connects to the target web catalog and parses the DOM to extract specific elements. It then utilizes Pandas to clean the raw data and structure it into a tabular format. Finally, SQLAlchemy establishes a local connection to push the clean DataFrame into an SQL table.