from app.models import LeadScoreInput

def score_lead(lead: LeadScoreInput) -> dict:
    score = 0
    reason = []

    if lead.days_since_created < 3:
        score += 25
        reason.append("Recently created lead")
    elif lead.days_since_created < 7:
        score += 15
    else:
        score += 5

    if lead.days_since_last_activity <= 2:
        score += 20
        reason.append("Recently active")
    elif lead.days_since_last_activity <= 5:
        score += 10

    if lead.quotation_amount >= 10000:
        score += 25
        reason.append("High deal value")
    elif lead.quotation_amount >= 5000:
        score += 15
    else:
        score += 5

    if lead.source == "referral":
        score += 10
        reason.append("Came from referral")

    if lead.past_meetings >= 2:
        score += 10
        reason.append("Multiple meetings held")

    score = min(score, 100)
    rating = "hot" if score >= 70 else "warm" if score >= 40 else "cold"

    return {
        "lead_id": lead.lead_id,
        "score": score,
        "rating": rating,
        "reasons": reason
    }
