from fastapi import FastAPI, Depends
from app.models import FollowUpPayload, LeadScoreInput, WinbackPayload, SummaryPayload
from app.auth import validate_api_key
from app.followup import handle_followup
from app.score import score_lead
from app.winback import handle_winback
from app.summary import handle_summary
from app.users import router as user_router
from app.database import init_db
from app.models import (
    ImproveEmailInput, LeadSummaryInput, EmailSequenceInput,
    ObjectionInput, CrmInsightInput, TranslateEmailInput
)
from app.handlers import (
    handle_improve_email, handle_lead_summary, handle_email_sequence,
    handle_objection_response, handle_crm_insight, handle_translation
)

app = FastAPI(title="Odoo AI Revenue Engine", version="1.0")

# 🔑 Register new users and init DB on startup
app.include_router(user_router)
init_db()

@app.get("/")
def root():
    return {"message": "Odoo AI Revenue Engine is live!"}

@app.post("/followup/generate", dependencies=[Depends(validate_api_key)])
def generate_followup(payload: FollowUpPayload):
    return handle_followup(payload)

@app.post("/lead/score", dependencies=[Depends(validate_api_key)])
def lead_score(payload: LeadScoreInput):
    return score_lead(payload)

@app.post("/winback/generate", dependencies=[Depends(validate_api_key)])
def generate_winback(payload: WinbackPayload):
    return handle_winback(payload)

@app.post("/summary/daily", dependencies=[Depends(validate_api_key)])
def generate_summary(payload: SummaryPayload):
    return handle_summary(payload)

@app.post("/email/improve", dependencies=[Depends(validate_api_key)])
def improve_email_route(payload: ImproveEmailInput):
    return handle_improve_email(payload)

@app.post("/lead/summary", dependencies=[Depends(validate_api_key)])
def lead_summary_route(payload: LeadSummaryInput):
    return handle_lead_summary(payload)

@app.post("/email/sequence", dependencies=[Depends(validate_api_key)])
def email_sequence_route(payload: EmailSequenceInput):
    return handle_email_sequence(payload)

@app.post("/deal/objection-handler", dependencies=[Depends(validate_api_key)])
def objection_handler_route(payload: ObjectionInput):
    return handle_objection_response(payload)

@app.post("/crm/insights", dependencies=[Depends(validate_api_key)])
def crm_insights_route(payload: CrmInsightInput):
    return handle_crm_insight(payload)

@app.post("/email/translate", dependencies=[Depends(validate_api_key)])
def translate_email_route(payload: TranslateEmailInput):
    return handle_translation(payload)
