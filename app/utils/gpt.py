import openai
from app.config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)


def generate_followup_email(lead_name: str, company: str, product: str, days_ago: int, tone: str = "friendly") -> str:
    prompt = f"""
    You are a helpful sales assistant.
    Write a {tone.lower()} follow-up email to {lead_name} from {company}.
    They received a quote for {product} {days_ago} days ago but haven’t responded.
    Offer to help, and suggest a quick call.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a {tone.lower()} sales assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_winback_email(lead_name: str, company: str, product: str, days_since_closed: int, reason_lost: str = "", tone: str = "friendly") -> str:
    prompt = f"""
    A deal with {lead_name} from {company} was lost {days_since_closed} days ago.
    They were interested in {product}. Reason for loss: {reason_lost or 'Not specified'}.
    Write a {tone.lower()} win-back email to see if the timing is better now.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are a {tone.lower()} sales rep."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_summary_email(user: str, opportunities: list) -> str:
    opportunity_descriptions = "\n".join([
        f"- {op.lead_name} from {op.company} (Quoted: ${op.quotation_amount}, Last contacted {op.days_since_last_contact} days ago, Stage: {op.stage})"
        for op in opportunities
    ])

    prompt = f"""
    You are a virtual sales assistant. Summarize the following opportunities for {user}.
    Highlight high-value leads, stale leads, and suggest daily follow-up actions.

    Opportunities:
    {opportunity_descriptions}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful sales assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def improve_email(raw_email: str, tone: str = "friendly") -> str:
    prompt = f"Improve the following email with a more {tone.lower()} tone, but keep its original meaning:\n\n{raw_email}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You're a {tone.lower()} sales copywriter."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_lead_summary(data: dict) -> str:
    prompt = f"""
    Analyze this lead and suggest next steps.
    Name: {data['lead_name']}, Company: {data['company']}, Quoted: {data['quotation_amount']}, 
    Last Contact: {data['last_contact_days']} days ago, Stage: {data['stage']}, Source: {data.get('source', 'N/A')}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_email_sequence(data: dict) -> str:
    tone = data.get("tone", "friendly")
    prompt = f"""
    Generate a 3-step email sequence for this campaign:
    - Campaign: {data['campaign_name']}
    - Audience: {data['audience']}
    - Goal: {data['goal']}
    - Tone: {tone}
    Make each email short, clear, and goal-oriented.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def handle_objection(data: dict) -> str:
    tone = data.get("tone", "friendly")
    prompt = f"""
    Handle this objection for the product {data['product']} from a {data.get('persona', 'customer')}:
    "{data['objection']}"
    Make it sound {tone.lower()} and convincing.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def crm_insight(data: dict) -> str:
    prompt = f"""
    Based on this lead data, suggest next-step actions:
    Stage: {data['lead_stage']}, Quotation: {data['quotation_amount']}, 
    Last Meeting: {data['last_meeting_days_ago']} days ago, Source: {data.get('source', 'N/A')}
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def translate_email(email_text: str, target_language: str) -> str:
    prompt = f"Translate this email into {target_language}:\n\n{email_text}"
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_next_best_action(data: dict) -> str:
    prompt = f"""
    You are a smart sales assistant. Based on the lead info below, suggest the next best action.

    Name: {data['lead_name']}
    Company: {data['company']}
    Stage: {data['stage']}
    Last Contact: {data['days_since_last_contact']} days ago
    Sentiment: {data.get('sentiment', 'neutral')}

    Suggest something concise like:
    - "Send pricing comparison"
    - "Book a demo"
    - "Pause follow-up 1 week"
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You're a proactive sales strategist."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()
