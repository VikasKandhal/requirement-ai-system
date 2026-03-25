# Default empty schema to ensure consistent output structure
EMPTY_SCHEMA = {
    "project_summary": [],
    "stakeholders": [],
    "deliverables": [],
    "functional_requirements": [],
    "non_functional_requirements": [],
    "constraints": [],
    "open_questions": []
}


# Function to normalize incoming data into expected schema format
def normalize_schema(data):
    """
    Guarantee the result is always a dict
    matching the expected schema shape.
    """

    # If model returned a list instead of dict,
    # treat it as functional requirements (safe fallback)
    if isinstance(data, list):
        return {
            **EMPTY_SCHEMA,
            "functional_requirements": data   # best safe default
        }

    # Create a copy of the empty schema to avoid mutation
    normalized = {**EMPTY_SCHEMA}

    # Iterate through all expected schema keys
    for key in normalized.keys():

        # If key exists in input and is a list,
        # copy its value into normalized output
        if key in data and isinstance(data[key], list):
            normalized[key] = data[key]

    # Return normalized schema
    return normalized