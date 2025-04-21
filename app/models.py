from typing import Optional, List
from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr


# 👇 Used for /followup/generate
class FollowUpPayload(BaseModel):
    lead_name: str
    company: str
    product: str
    days_ago: Optional[int] = 3
    tone: Optional[str] = "friendly"  # 🆕


# 👇 Used for /lead/score
class LeadScoreInput(BaseModel):
    lead_id: str
    days_since_created: int
    days_since_last_activity: int
    quotation_amount: float
    source: Optional[str] = None
    past_meetings: Optional[int] = 0


# 👇 Used for /winback/generate
class WinbackPayload(BaseModel):
    lead_name: str
    company: str
    product: str
    days_since_closed: int
    reason_lost: Optional[str] = None
    tone: Optional[str] = "friendly"  # 🆕


# 👇 Used for /summary/daily
class Opportunity(BaseModel):
    lead_name: str
    company: str
    quotation_amount: float
    days_since_last_contact: int
    stage: str

class SummaryPayload(BaseModel):
    user: str
    opportunities: List[Opportunity]


# 1. Email Improver
class ImproveEmailInput(BaseModel):
    raw_email: str
    tone: Optional[str] = "friendly"  # 🆕


# 2. Lead Summary Strategist
class LeadSummaryInput(BaseModel):
    lead_name: str
    company: str
    quotation_amount: float
    last_contact_days: int
    stage: str
    source: Optional[str] = None


# 3. Email Sequence Generator
class EmailSequenceInput(BaseModel):
    campaign_name: str
    audience: str
    goal: str
    tone: Optional[str] = "friendly"  # 🆕


# 4. Objection Handler
class ObjectionInput(BaseModel):
    objection: str
    product: str
    persona: Optional[str] = None
    tone: Optional[str] = "friendly"  # 🆕


# 5. CRM Insights
class CrmInsightInput(BaseModel):
    lead_stage: str
    quotation_amount: float
    last_meeting_days_ago: int
    source: Optional[str] = None


# 6. Email Translator
class TranslateEmailInput(BaseModel):
    email_text: str
    target_language: str


# 7. Next Best Action
class NextBestActionInput(BaseModel):
    lead_name: str
    company: str
    stage: str
    days_since_last_contact: int
    sentiment: Optional[str] = "neutral"
