# Default schema for risk analysis output
# Ensures consistent structure with required keys
RISK_SCHEMA = {
    "risks": [],
    "clarifications_needed": []
}

# Function to normalize and validate risk analysis result
def normalize_risk_result(data):

    # If input is not a dictionary, return default schema
    if not isinstance(data, dict):
        return RISK_SCHEMA.copy()

    # Create a copy of schema to avoid modifying original
    result = RISK_SCHEMA.copy()

    # Check if "risks" key exists and is a list
    # If valid, assign it to result
    if "risks" in data and isinstance(data["risks"], list):
        result["risks"] = data["risks"]

    # Check if "clarifications_needed" key exists and is a list
    # If valid, assign it to result
    if "clarifications_needed" in data and isinstance(data["clarifications_needed"], list):
        result["clarifications_needed"] = data["clarifications_needed"]

    # Return normalized result
    return result