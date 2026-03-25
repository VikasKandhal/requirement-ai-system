"""
extractor.py

This module is responsible for extracting structured requirements from
unstructured text using a Large Language Model (LLM).

Key Responsibilities:
- Convert raw user input into categorized requirement data
- Classify information into predefined categories such as:
  - Business Objectives
  - Functional Requirements
  - Non-Functional Requirements
  - Constraints & Assumptions
  - Open Questions
- Ensure strict adherence to factual extraction without inference

How it works:
- A carefully engineered prompt is constructed with explicit rules
- The prompt is sent to an LLM via the Groq API
- The model processes the input text and returns structured JSON output
- The response is parsed into a Python dictionary for downstream processing

Important Design Considerations:
- Prompt engineering is used to control output format and accuracy
- Strict JSON structure ensures compatibility with pipeline processing
- Source traceability is maintained using "source_quote" for each item
- No assumptions or inferred data are allowed to maintain data integrity

Why this module is critical:
- It acts as the core intelligence layer of the system
- The quality of extracted requirements directly impacts downstream tasks
  like risk analysis and task planning
- Enables automation of requirement analysis from natural language input

Limitations:
- Dependent on LLM response consistency
- Requires strict prompt design to avoid malformed JSON
- Performance depends on API latency and model behavior
"""

from groq import Groq
from services.config import GROK_API_KEY
from dotenv import load_dotenv

load_dotenv()

import os


import json

client = Groq(api_key=os.getenv("GROK_API_KEY"))

def extract_requirements(text):
    prompt = f"""
Classify extracted information into the correct category.

Follow these rules:
Functional Requirements = system capabilities / actions
Non-Functional Requirements = performance, scale, reliability, security
Constraints & Assumptions = external limits, dependencies, scope boundaries
Business Objectives = goals, motivations, outcomes

Do NOT infer or assume.
Extract only what appears in the text.

Constraints & Assumptions include:
technology limitations
operational assumptions
environment constraints
scope exclusions
dependencies on external parties
language or region restrictions
data ownership or responsibility
anything marked “assumption”

If an item begins with "Assumption", "Client assumption",
or appears in an assumption section — classify it under constraints_and_assumptions.

For source_quote:
-It must contain the exact sentence or phrase that expresses the requirement.
-Do NOT use section headers, labels, or titles as source quotes.
-The quote must come from the same sentence as the requirement value.
If a requirement value cannot be directly matched to a sentence,
do NOT include it.



Return STRICT JSON in this structure:

{{
  "business_objectives": [],
  "functional_requirements": [],
  "non_functional_requirements": [],
  "constraints_and_assumptions": [],
  "open_questions": []
}}

For each item include:
"value" and "source_quote".

Text:
{text}
"""


    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "You extract strictly factual requirements from text."},
            {"role": "user", "content": prompt}
        ]
    )

    output = response.choices[0].message.content

    # convert JSON string → python dict
    return json.loads(output)



