import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('sqlite:///products_database.db')

sql_query = "SELECT * FROM books_table"

table_data = pd.read_sql(sql_query, con=engine)

print("\n--- READING DATA DIRECTLY FROM THE DATABASE ---")
print(table_data)