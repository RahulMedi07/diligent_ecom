
from faker import Faker
import pandas as pd
import random

fake = Faker()

# Customers
customers = [{'customer_id': i+1, 'name': fake.name(), 'email': fake.email()} for i in range(50)]
pd.DataFrame(customers).to_csv('customers.csv', index=False)

# Products
products = [{'product_id': i+1, 'name': fake.word(), 'price': round(random.uniform(10, 500),2)} for i in range(50)]
pd.DataFrame(products).to_csv('products.csv', index=False)

# Orders
orders = [{'order_id': i+1, 'customer_id': random.randint(1,50)} for i in range(50)]
pd.DataFrame(orders).to_csv('orders.csv', index=False)

# Order Items
order_items = [{'order_item_id': i+1, 'order_id': random.randint(1,50), 'product_id': random.randint(1,50), 'quantity': random.randint(1,5)} for i in range(100)]
pd.DataFrame(order_items).to_csv('order_items.csv', index=False)

# Reviews
reviews = [{'review_id': i+1, 'product_id': random.randint(1,50), 'customer_id': random.randint(1,50), 'rating': random.randint(1,5)} for i in range(50)]
pd.DataFrame(reviews).to_csv('reviews.csv', index=False)
