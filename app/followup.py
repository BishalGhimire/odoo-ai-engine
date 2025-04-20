from app.utils.gpt import generate_followup_email
from app.models import FollowUpPayload


def handle_followup(payload: FollowUpPayload):
    return {"email": generate_followup_email(
        payload.lead_name,
        payload.company,
        payload.product,
        payload.days_ago
    )}