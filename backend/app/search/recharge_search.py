import pandas as pd
from pathlib import Path

RECHARGE_FILE = Path("../documents/csv/recharge_transactions.csv")

recharges = pd.read_csv(RECHARGE_FILE)


def search_recharge(customer_id):

    result = recharges[
        recharges["customer_id"].astype(str).str.upper()
        == customer_id.upper()
    ]

    if result.empty:
        return None

    return result.to_dict(orient="records")
