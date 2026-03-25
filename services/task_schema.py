# Default schema for task output
# Ensures the response always contains an "epics" key
TASK_SCHEMA = {
    "epics": []
}

# Function to normalize and validate task result data
def normalize_task_result(data):

    # Check if input is not a dictionary
    # If invalid, return a copy of the default schema
    if not isinstance(data, dict):
        return TASK_SCHEMA.copy()

    # Create a copy of the default schema to avoid modifying original
    result = TASK_SCHEMA.copy()

    # Check if "epics" key exists and is a list
    # If valid, assign it to result
    if "epics" in data and isinstance(data["epics"], list):
        result["epics"] = data["epics"]

    # Return normalized result
    return result