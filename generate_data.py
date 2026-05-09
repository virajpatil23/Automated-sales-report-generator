import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

random.seed(42)
np.random.seed(42)

products = ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Headphones',
            'Webcam', 'USB Hub', 'Desk Lamp', 'Notebook', 'Pen Drive']
regions = ['North', 'South', 'East', 'West']

rows = []
start_date = datetime(2025, 1, 1)

for i in range(500):
    date = start_date + timedelta(days=random.randint(0, 90))
    product = random.choice(products)
    region = random.choice(regions)
    quantity = random.randint(1, 20)
    unit_price = round(random.uniform(50, 1500), 2)
    revenue = round(quantity * unit_price, 2)
    rows.append([date.strftime('%Y-%m-%d'), product, region, quantity, unit_price, revenue])

df = pd.DataFrame(rows, columns=['Date', 'Product', 'Region', 'Quantity', 'UnitPrice', 'Revenue'])
df.to_csv('sales_data.csv', index=False)
print("sales_data.csv created with", len(df), "rows")