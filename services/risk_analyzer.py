# Import JSON module for parsing model output
import json

# Import Groq client for LLM interaction
from groq import Groq

# Import API key config (not directly used here but part of config setup)
from services.config import GROK_API_KEY

# Load environment variables from .env file
from dotenv import load_dotenv

load_dotenv()

# Import os to access environment variables
import os

# Initialize Groq client using API key from environment
client = Groq(api_key=os.getenv("GROK_API_KEY"))


# Function to analyze risks from input requirement text
def analyze_risks(text: str):
    """
    Risk & Dependency Analyzer
    Returns grounded, structured risk insights.
    """

    # Construct prompt for LLM with strict instructions
    prompt = f"""
You are a risk & ambiguity analysis assistant for software requirement documents.

Analyze ONLY the information explicitly present in the text.
Do NOT infer, assume, or speculate.

Identify:
- ambiguity risks
- dependency risks
- scope risks
- technical risks
- operational risks
- missing acceptance criteria
- undefined responsibilities
- vague requirement wording

For each risk, include:
- type  (business | technical | operational | dependency | scope | UX | security)
- description  (short + factual)
- source_quote  (exact phrase from text — not a section heading)
- impact  (low | medium | high)
- recommended_action  (what clarification or follow-up is needed)

If no risks exist, return an empty list.

Return STRICT JSON in this format:

{{
  "risks": [
    {{
      "type": "",
      "description": "",
      "source_quote": "",
      "impact": "",
      "recommended_action": ""
    }}
  ],
  "clarifications_needed": []
}}

Text to analyze:
{text}
"""

    # Send request to Groq LLM API
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            # System role defines behavior of the model
            {"role": "system", "content": "You analyze requirement risks with evidence-grounded reasoning only."},

            # User role contains the actual prompt
            {"role": "user", "content": prompt}
        ]
    )

    # Extract response content from API result
    output = response.choices[0].message.content

    # Convert JSON string output into Python dictionary
    return json.loads(output)