import pandas as pd
from pathlib import Path

COMPLAINT_FILE = Path("../documents/csv/complaint_tickets.csv")

complaints = pd.read_csv(COMPLAINT_FILE)


def search_complaint(request_id):
    result = complaints[
        complaints["request_id"].astype(str) == str(request_id)
    ]

    if result.empty:
        return None

    return result.iloc[0].to_dict()