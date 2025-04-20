from fastapi import FastAPI, Depends
from app.models import FollowUpPayload, LeadScoreInput, WinbackPayload, SummaryPayload
from app.auth import validate_api_key
from app.followup import handle_followup
from app.score import score_lead
from app.winback import handle_winback
from app.summary import handle_summary

app = FastAPI(title="Odoo AI Revenue Engine", version="1.0")

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
