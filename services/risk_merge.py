# Function to merge incoming risks into master list without duplicates
def merge_risks(master, incoming):

    # Create a set of already seen risks using (description, source_quote)
    # This helps in fast lookup to avoid duplicates
    seen = {(r["description"], r["source_quote"]) for r in master}

    # Iterate through incoming risks
    for r in incoming:

        # Create a unique key for each risk
        key = (r["description"], r["source_quote"])

        # If risk is not already seen, add it to master list
        if key not in seen:
            master.append(r)

            # Mark this risk as seen to prevent future duplicates
            seen.add(key)

    # Return updated master list
    return master