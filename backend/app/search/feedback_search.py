import pandas as pd
from pathlib import Path

FEEDBACK_FILE = Path("../documents/csv/customer_feedback.csv")

feedback = pd.read_csv(FEEDBACK_FILE)


def search_feedback(customer_id):

    result = feedback[
        feedback["customer_id"].astype(str).str.upper()
        == customer_id.upper()
    ]

    if result.empty:
        return None

    return result.to_dict(orient="records")