import pandas as pd
from pathlib import Path

SERVICE_FILE = Path("../documents/csv/service_requests.csv")

services = pd.read_csv(SERVICE_FILE)


def search_service(customer_id):

    result = services[
        services["customer_id"].astype(str).str.upper()
        == customer_id.upper()
    ]

    if result.empty:
        return None

    return result.to_dict(orient="records")