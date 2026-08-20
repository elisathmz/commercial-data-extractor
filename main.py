import requests
from bs4 import BeautifulSoup
import pandas as pd
from sqlalchemy import create_engine

url = "http://books.toscrape.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

products = soup.find_all("article", class_="product_pod")
extracted_data = []

for product in products[:5]:
    title = product.h3.a["title"]
    raw_price = product.find("p", class_="price_color").text
    clean_price = raw_price.replace("Â£", "").replace("£", "")
    
    extracted_data.append({
        "Product Name": title,
        "Clean Price": clean_price
    })

table = pd.DataFrame(extracted_data)

engine = create_engine('sqlite:///products_database.db')

table.to_sql('books_table', con=engine, if_exists='replace', index=False)

print("\n--- DATA SUCCESSFULLY SAVED TO DATABASE! ---")