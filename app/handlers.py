from app.utils.gpt import (
    improve_email,
    generate_lead_summary,
    generate_email_sequence,
    handle_objection,
    crm_insight,
    translate_email
)
from app.models import NextBestActionInput
from app.utils.gpt import generate_next_best_action

def handle_improve_email(payload):
    return {"improved_email": improve_email(payload.raw_email)}

def handle_lead_summary(payload):
    return {"summary": generate_lead_summary(payload.dict())}

def handle_email_sequence(payload):
    return {"sequence": generate_email_sequence(payload.dict())}

def handle_objection_response(payload):
    return {"response": handle_objection(payload.dict())}

def handle_crm_insight(payload):
    return {"insight": crm_insight(payload.dict())}

def handle_translation(payload):
    return {"translated": translate_email(payload.email_text, payload.target_language)}



def handle_next_best_action(payload: NextBestActionInput):
    return {"recommendation": generate_next_best_action(payload.dict())}

