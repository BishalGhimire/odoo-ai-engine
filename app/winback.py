from app.models import WinbackPayload
from app.utils.gpt import generate_winback_email

def handle_winback(payload: WinbackPayload):
    return {
        "email": generate_winback_email(
            lead_name=payload.lead_name,
            company=payload.company,
            product=payload.product,
            days_since_closed=payload.days_since_closed,
            reason_lost=payload.reason_lost
        )
    }
