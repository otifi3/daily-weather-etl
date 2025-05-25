import pandas as pd
import logging
import os

logging.basicConfig(level=logging.INFO)

def load_to_csv(df, filename="etl_output.csv"):
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', index=False, header=False)
    else:
        df.to_csv(filename, index=False)
    logging.info(f"✅ Data loaded into {filename}")
