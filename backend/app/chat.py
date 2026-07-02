from fastapi import APIRouter
from pydantic import BaseModel
import re

from app.rag.rag_chain import get_rag_chain

from app.search.customer_search import search_customer
from app.search.complaint_search import search_complaint
from app.search.billing_search import search_bill
from app.search.recharge_search import search_recharge
from app.search.mobile_search import search_mobile
from app.search.service_search import search_service
from app.search.feedback_search import search_feedback

router = APIRouter()


class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    question = request.question.strip()
    question_upper = question.upper()

    # ======================================
    # CUSTOMER SEARCH
    # ======================================

    customer_match = re.search(r"(CUST\d+)", question_upper)

    if (
        customer_match
        and "BILL" not in question_upper
        and "RECHARGE" not in question_upper
        and "MOBILE" not in question_upper
        and "SERVICE" not in question_upper
        and "FEEDBACK" not in question_upper
    ):

        customer_id = customer_match.group(1)

        customer = search_customer(customer_id)

        if customer:

            answer = "👤 CUSTOMER DETAILS\n\n"

            for key, value in customer.items():
                answer += f"• {key}: {value}\n"

            return {
                "question": question,
                "answer": answer
            }

        return {
            "question": question,
            "answer": f"❌ Customer {customer_id} not found."
        }

    # ======================================
    # COMPLAINT SEARCH
    # ======================================

    complaint_match = re.search(
        r"REQUEST\s*ID\s*(\d+)|COMPLAINT\s*(\d+)",
        question_upper
    )

    if complaint_match:

        request_id = complaint_match.group(1) or complaint_match.group(2)

        complaint = search_complaint(request_id)

        if complaint:

            answer = "📋 COMPLAINT DETAILS\n\n"

            for key, value in complaint.items():
                answer += f"• {key}: {value}\n"

            return {
                "question": question,
                "answer": answer
            }

        return {
            "question": question,
            "answer": f"❌ Complaint Request ID {request_id} not found."
        }

    # ======================================
    # BILLING SEARCH
    # ======================================

    if "BILL" in question_upper or "BILLING" in question_upper:

        customer_match = re.search(r"(CUST\d+)", question_upper)

        if customer_match:

            customer_id = customer_match.group(1)

            bills = search_bill(customer_id)

            if bills:

                answer = f"💰 BILLING HISTORY - {customer_id}\n\n"

                for i, bill in enumerate(bills, 1):

                    answer += f"Bill {i}\n"

                    for key, value in bill.items():
                        answer += f"• {key}: {value}\n"

                    answer += "\n"

                return {
                    "question": question,
                    "answer": answer
                }

            return {
                "question": question,
                "answer": f"❌ No billing records found for {customer_id}."
            }

    # ======================================
    # RECHARGE SEARCH
    # ======================================

    if "RECHARGE" in question_upper:

        customer_match = re.search(r"(CUST\d+)", question_upper)

        if customer_match:

            customer_id = customer_match.group(1)

            recharges = search_recharge(customer_id)

            if recharges:

                answer = f"💳 RECHARGE HISTORY - {customer_id}\n\n"

                for i, recharge in enumerate(recharges, 1):

                    answer += f"Recharge {i}\n"

                    for key, value in recharge.items():
                        answer += f"• {key}: {value}\n"

                    answer += "\n"

                return {
                    "question": question,
                    "answer": answer
                }

            return {
                "question": question,
                "answer": f"❌ No recharge history found for {customer_id}."
            }

    # ======================================
    # MOBILE SEARCH
    # ======================================

    if "MOBILE" in question_upper:

        customer_match = re.search(r"(CUST\d+)", question_upper)

        if customer_match:

            customer_id = customer_match.group(1)

            mobile = search_mobile(customer_id)

            if mobile:

                answer = f"📱 MOBILE CONNECTIONS - {customer_id}\n\n"

                for i, connection in enumerate(mobile, 1):

                    answer += f"Connection {i}\n"

                    for key, value in connection.items():
                        answer += f"• {key}: {value}\n"

                    answer += "\n"

                return {
                    "question": question,
                    "answer": answer
                }

            return {
                "question": question,
                "answer": f"❌ No mobile connection found for {customer_id}."
            }

    # ======================================
    # SERVICE REQUEST SEARCH
    # ======================================

    if "SERVICE" in question_upper:

        customer_match = re.search(r"(CUST\d+)", question_upper)

        if customer_match:

            customer_id = customer_match.group(1)

            services = search_service(customer_id)

            if services:

                answer = f"🛠️ SERVICE REQUESTS - {customer_id}\n\n"

                for i, service in enumerate(services, 1):

                    answer += f"Request {i}\n"

                    for key, value in service.items():
                        answer += f"• {key}: {value}\n"

                    answer += "\n"

                return {
                    "question": question,
                    "answer": answer
                }

            return {
                "question": question,
                "answer": f"❌ No service requests found for {customer_id}."
            }

    # ======================================
    # CUSTOMER FEEDBACK SEARCH
    # ======================================

    if "FEEDBACK" in question_upper:

        customer_match = re.search(r"(CUST\d+)", question_upper)

        if customer_match:

            customer_id = customer_match.group(1)

            feedbacks = search_feedback(customer_id)

            if feedbacks:

                answer = f"⭐ CUSTOMER FEEDBACK - {customer_id}\n\n"

                for i, feedback in enumerate(feedbacks, 1):

                    answer += f"Feedback {i}\n"

                    for key, value in feedback.items():
                        answer += f"• {key}: {value}\n"

                    answer += "\n"

                return {
                    "question": question,
                    "answer": answer
                }

            return {
                "question": question,
                "answer": f"❌ No customer feedback found for {customer_id}."
            }

    # ======================================
    # RAG SEARCH
    # ======================================

    qa_chain = get_rag_chain()

    response = qa_chain.invoke(
        {"query": question}
    )

    return {
        "question": question,
        "answer": response["result"]
    }