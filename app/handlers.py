from app.utils.gpt import (
    improve_email,
    generate_lead_summary,
    generate_email_sequence,
    handle_objection,
    crm_insight,
    translate_email,
    generate_next_best_action,
    generate_followup_email,
    generate_winback_email,
    generate_summary_email,
)

def handle_improve_email(payload):
    return {
        "improved_email": improve_email(payload.raw_email, payload.tone)
    }

def handle_lead_summary(payload):
    return {
        "summary": generate_lead_summary(payload.dict())
    }

def handle_email_sequence(payload):
    return {
        "sequence": generate_email_sequence(payload.dict())
    }

def handle_objection_response(payload):
    return {
        "response": handle_objection(payload.dict())
    }

def handle_crm_insight(payload):
    return {
        "insight": crm_insight(payload.dict())
    }

def handle_translation(payload):
    return {
        "translated": translate_email(payload.email_text, payload.target_language)
    }

def handle_next_best_action(payload):
    return {
        "action": generate_next_best_action(payload.dict())
    }

def handle_followup(payload):
    return {
        "email": generate_followup_email(
            payload.lead_name,
            payload.company,
            payload.product,
            payload.days_ago,
            payload.tone
        )
    }

def handle_winback(payload):
    return {
        "email": generate_winback_email(
            payload.lead_name,
            payload.company,
            payload.product,
            payload.days_since_closed,
            payload.reason_lost or "",
            payload.tone
        )
    }

def handle_summary(payload):
    return {
        "summary": generate_summary_email(payload.user, payload.opportunities)
    }
