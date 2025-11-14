import sqlite3
import pandas as pd

conn = sqlite3.connect('ecommerce.db')

files = ['customers.csv','products.csv','orders.csv','order_items.csv','reviews.csv']
for f in files:
    df = pd.read_csv(f)
    df.to_sql(f.split('.')[0], conn, if_exists='replace', index=False)

conn.close()
print("Data ingested into SQLite successfully!")

