import pandas as pd
from pathlib import Path

# Path to customer CSV
CUSTOMER_FILE = Path("../documents/csv/customer_master.csv")

# Load only once
customers = pd.read_csv(CUSTOMER_FILE)


def search_customer(customer_id: str):
    result = customers[
        customers["customer_id"].astype(str).str.upper()
        == customer_id.upper()
    ]

    if result.empty:
        return None

    return result.iloc[0].to_dict()