from fastapi import APIRouter
import pandas as pd
from pathlib import Path

router = APIRouter()


CSV_PATH = Path("../documents/csv")

customers = pd.read_csv(CSV_PATH / "customer_master.csv")
complaints = pd.read_csv(CSV_PATH / "complaint_tickets.csv")
recharges = pd.read_csv(CSV_PATH / "recharge_transactions.csv")
mobile = pd.read_csv(CSV_PATH / "mobile_connections.csv")
service = pd.read_csv(CSV_PATH / "service_requests.csv")
feedback = pd.read_csv(CSV_PATH / "customer_feedback.csv")


@router.get("/analytics")
def analytics():

    return {

        "total_customers": len(customers),

        "active_customers":
        len(customers[customers["status"] == "Active"]),

        "total_mobile_connections":
        len(mobile),

        "total_complaints":
        len(complaints),

        "total_service_requests":
        len(service),

        "total_recharges":
        len(recharges),

        "total_recharge_amount":
        float(recharges["amount"].sum()),

        "average_feedback":
        round(feedback["rating"].mean(),2)

    }