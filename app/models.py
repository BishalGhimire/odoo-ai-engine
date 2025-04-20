from pydantic import BaseModel
from typing import Optional
from typing import List
from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr


# 👇 Used for /followup/generate
class FollowUpPayload(BaseModel):
    lead_name: str
    company: str
    product: str
    days_ago: Optional[int] = 3

# 👇 Used for /lead/score
class LeadScoreInput(BaseModel):
    lead_id: str
    days_since_created: int
    days_since_last_activity: int
    quotation_amount: float
    source: Optional[str] = None  # e.g. 'referral', 'web', etc.
    past_meetings: Optional[int] = 0

# 👇 Used for /winback/generate
class WinbackPayload(BaseModel):
    lead_name: str
    company: str
    product: str
    days_since_closed: int
    reason_lost: Optional[str] = None



class Opportunity(BaseModel):
    lead_name: str
    company: str
    quotation_amount: float
    days_since_last_contact: int
    stage: str  # e.g., "Negotiation", "Proposal", "Follow-Up"

class SummaryPayload(BaseModel):
    user: str
    opportunities: List[Opportunity]

# 1. Email Improver
class ImproveEmailInput(BaseModel):
    raw_email: str

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

# 4. Objection Handler
class ObjectionInput(BaseModel):
    objection: str
    product: str
    persona: Optional[str] = None

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
