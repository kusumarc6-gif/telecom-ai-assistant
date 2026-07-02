import pandas as pd
from pathlib import Path

MOBILE_FILE = Path("../documents/csv/mobile_connections.csv")

mobile = pd.read_csv(MOBILE_FILE)


def search_mobile(customer_id):

    result = mobile[
        mobile["customer_id"].astype(str).str.upper()
        == customer_id.upper()
    ]

    if result.empty:
        return None

    return result.to_dict(orient="records")