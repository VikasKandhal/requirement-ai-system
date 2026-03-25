"""
merge_utils.py

This module provides utility functions to merge structured extraction results
generated from multiple chunks of input text (e.g., large documents or PDFs).

Key Responsibilities:
- Combine results from different chunks into a single unified structure
- Prevent duplicate entries using a combination of "value" and "source_quote"
- Maintain data integrity while aggregating results across processing stages

How it works:
- Each chunk produces partial structured output (requirements, risks, etc.)
- These outputs are merged incrementally into a master result
- Duplicate entries are avoided using a set-based lookup for efficiency

This approach ensures scalable and consistent aggregation of AI-generated data
when processing large inputs in a chunked pipeline.
"""

def merge_list_items(existing_list, new_list):
    """
    Avoid duplicates by comparing value + source_quote.
    """
    seen = {(item["value"], item["source_quote"]) for item in existing_list}

    for item in new_list:
        key = (item["value"], item["source_quote"])
        if key not in seen and item["value"].strip():
            existing_list.append(item)
            seen.add(key)

    return existing_list


def merge_extractions(master, incoming):
    """
    Merge structured extraction results chunk-by-chunk.
    """

    for field in master.keys():

        # skip fields that are not lists
        if not isinstance(master[field], list):
            continue

        new_items = incoming.get(field, [])

        merge_list_items(master[field], new_items)

    return master
