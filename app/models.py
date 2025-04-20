from pydantic import BaseModel
from typing import Optional
from typing import List


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

