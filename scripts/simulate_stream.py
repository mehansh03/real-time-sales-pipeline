import pandas as pd
import time
from datetime import datetime

chunk_size = 100
for chunk in pd.read_csv("data/raw/sales_data.csv", chunksize=chunk_size):
    chunk.to_json("data/raw/stream_chunk.json", orient="records")
    print(f"Processed chunk at {datetime.now()}")
    time.sleep(5)  