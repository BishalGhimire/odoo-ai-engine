from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import List, Optional
from app.auth import validate_api_key
from app.utils.gpt import client

router = APIRouter()


# 1. 📋 /meeting/recap
class MeetingRecapInput(BaseModel):
    notes: str

@router.post("/meeting/recap", dependencies=[Depends(validate_api_key)])
def meeting_recap(payload: MeetingRecapInput):
    prompt = f"""
    You are a business assistant. Summarize the meeting notes below into:
    - A brief recap
    - Key decisions made
    - Follow-up action items

    Notes:
    {payload.notes}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"recap": response.choices[0].message.content.strip()}


# 2. 🏷️ /email/classify
class EmailClassifyInput(BaseModel):
    email: str

@router.post("/email/classify", dependencies=[Depends(validate_api_key)])
def classify_email(payload: EmailClassifyInput):
    prompt = f"""
    Classify the intent of this email. Return the tag only, such as: demo_request, pricing, support, spam, unsubscribe, feedback.

    Email:
    {payload.email}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"tag": response.choices[0].message.content.strip()}


# 3. 💬 /linkedin/rewrite
class LinkedInRewriteInput(BaseModel):
    message: str

@router.post("/linkedin/rewrite", dependencies=[Depends(validate_api_key)])
def rewrite_linkedin(payload: LinkedInRewriteInput):
    prompt = f"""
    Rewrite the following LinkedIn outreach message to sound more casual, shorter, and increase chances of reply:

    Message:
    {payload.message}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"rewritten": response.choices[0].message.content.strip()}


# 4. 🎯 /lead/fit-score
class LeadFitScoreInput(BaseModel):
    industry: str
    size: str
    region: Optional[str] = None
    use_case: Optional[str] = None

@router.post("/lead/fit-score", dependencies=[Depends(validate_api_key)])
def fit_score(payload: LeadFitScoreInput):
    prompt = f"""
    Based on this lead info and assuming the ideal customer is a mid-size SaaS business in North America, return a fit score (0-100) with a one-line reason.

    Industry: {payload.industry}
    Size: {payload.size}
    Region: {payload.region}
    Use case: {payload.use_case}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"fit_score": response.choices[0].message.content.strip()}


# 5. ⚔️ /comparison/email
class ComparisonEmailInput(BaseModel):
    competitor: str
    product: str
    customer_use_case: str

@router.post("/comparison/email", dependencies=[Depends(validate_api_key)])
def comparison_email(payload: ComparisonEmailInput):
    prompt = f"""
    Write an email that highlights why {payload.product} is a better option than {payload.competitor}, focused on this use case: {payload.customer_use_case}.
    Make it persuasive but not overly aggressive.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"email": response.choices[0].message.content.strip()}


# 6. 🧾 /proposal/draft
class ProposalDraftInput(BaseModel):
    client_name: str
    product: str
    features: List[str]
    price: float

@router.post("/proposal/draft", dependencies=[Depends(validate_api_key)])
def proposal_draft(payload: ProposalDraftInput):
    features_str = ", ".join(payload.features)
    prompt = f"""
    Draft a proposal for {payload.client_name} about purchasing {payload.product}.
    Include benefits of features: {features_str}, and price: ${payload.price}
    Make it sound professional and ready-to-send.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return {"proposal": response.choices[0].message.content.strip()}


# 7. 📊 /usage/summary
@router.get("/usage/summary", dependencies=[Depends(validate_api_key)])
def usage_summary():
    # In real use case, you'd pull from DB or API logs
    return {
        "total_calls": 132,
        "top_endpoints": ["/followup/generate", "/lead/score", "/email/improve"],
        "monthly_usage": "32 calls this month"
    }


# 8. 🔗 /slack/webhook
class SlackWebhookInput(BaseModel):
    text: str

@router.post("/slack/webhook")
def slack_webhook(payload: SlackWebhookInput):
    # Simple echo for now — could route to GPT or CRM
    return {"response": f"You said: {payload.text}"}
