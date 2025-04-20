from app.models import SummaryPayload
from app.utils.gpt import generate_summary_email

def handle_summary(payload: SummaryPayload):
    return {
        "summary": generate_summary_email(
            user=payload.user,
            opportunities=payload.opportunities
        )
    }
