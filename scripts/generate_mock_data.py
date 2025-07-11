from faker import Faker
import json
import pandas as pd
from datetime import datetime

fake = Faker()
data = []
for i in range(1000): 
    record = {
        "order_id": fake.uuid4(),
        "customer_id": fake.uuid4(),
        "product_id": fake.uuid4(),
        "product_name": fake.word(),
        "category": fake.random_element(["Electronics", "Clothing", "Books"]),
        "price": round(fake.random_number(digits=4) / 100, 2),
        "quantity": fake.random_int(min=1, max=10),
        "timestamp": datetime.now().isoformat(),
        "region": fake.random_element(["North", "South", "East", "West"])
    }
    data.append(record)

with open("data/raw/sales_data.json", "w") as f:
    json.dump(data, f)
pd.DataFrame(data).to_csv("data/raw/sales_data.csv", index=False)