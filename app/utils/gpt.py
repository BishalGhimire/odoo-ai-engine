import openai
from app.config import OPENAI_API_KEY

client = openai.OpenAI(api_key=OPENAI_API_KEY)


def generate_followup_email(lead_name: str, company: str, product: str, days_ago: int) -> str:
    prompt = f"""
    You are a helpful sales assistant.
    Write a professional and friendly follow-up email to {lead_name} from {company}.
    They received a quote for {product} {days_ago} days ago but haven't responded.
    Gently offer to answer questions and suggest a quick call to assist.
    """
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful sales assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content.strip()


def generate_winback_email(lead_name: str, company: str, product: str, days_since_closed: int, reason_lost: str = "") -> str:
    prompt = f"""
    You are a sales assistant. A deal with {lead_name} from {company} was lost {days_since_closed} days ago.
    The product they were interested in was {product}. Reason for loss: {reason_lost if reason_lost else 'Not specified'}.
    Write a warm and open-minded win-back email, expressing interest in revisiting the conversation if the timing is better now.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful sales assistant."},
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
    Highlight high-value leads, stale leads (not contacted recently), and suggest daily follow-up actions.

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
