import pandas as pd
from pathlib import Path

BILL_FILE = Path("../documents/csv/billing_history.csv")

billing = pd.read_csv(BILL_FILE)


def search_bill(customer_id):

    result = billing[
        billing["customer_id"].astype(str).str.upper()
        == customer_id.upper()
    ]

    if result.empty:
        return None

    return result.to_dict(orient="records")