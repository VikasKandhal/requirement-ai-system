"""
pipeline.py

This module acts as the central orchestration layer of the system.
It coordinates multiple services to process user input (text or PDF)
and generate structured outputs including requirements, risks, and task plans.

Pipeline Flow:
1. Input ingestion (text or PDF)
2. Text chunking (for large inputs)
3. Requirement extraction
4. Risk analysis
5. Task planning
6. Aggregation of results

This modular pipeline design ensures scalability and maintainability.
"""

# Import service modules responsible for each stage of processing
from services.extractor import extract_requirements   # Extract structured requirements from text
from services.risk_analyzer import analyze_risks      # Identify risks from input
from services.task_planner import plan_tasks          # Generate actionable tasks

# Import utilities for handling PDF input and large text processing
from services.pdf_reader import read_pdf_text         # Extract text from PDF files
from services.chunker import chunk_text               # Split large text into manageable chunks


def run_pipeline(text: str = None, pdf_path: str = None):
    """
    Main pipeline function to process user input.

    Supports two types of input:
    - Plain text input
    - PDF file input (processed in chunks)

    Args:
        text (str): Raw user input text
        pdf_path (str): Path to PDF file

    Returns:
        dict: Aggregated results including:
            - Number of chunks processed
            - Extracted requirements
            - Identified risks
            - Generated task plan
    """

    # Step 1: Input Handling
    # If PDF is provided, extract full text and split into chunks
    if pdf_path:
        full_text = read_pdf_text(pdf_path)   # Extract text from PDF
        chunks = chunk_text(full_text)        # Break into smaller chunks for processing
    else:
        # If plain text is provided, wrap it into a single chunk list
        chunks = [text]

    # Step 2: Initialize containers to store aggregated results
    all_requirements = []
    all_risks = []
    all_tasks = []

    # Step 3: Process each chunk independently
    # This improves scalability for large inputs (like PDFs)
    for chunk in chunks:

        # Extract structured requirements from the chunk
        req = extract_requirements(chunk)

        # Analyze potential risks from the same chunk
        risk = analyze_risks(chunk)

        # Generate task plan based on requirements and risks
        task = plan_tasks(req, risk)

        # Store results for each chunk
        all_requirements.append(req)
        all_risks.append(risk)
        all_tasks.append(task)

    # Step 4: Return aggregated output
    return {
        "chunks_processed": len(chunks),   # Total number of processed chunks
        "requirements": all_requirements,  # List of requirements per chunk
        "risks": all_risks,                # List of risks per chunk
        "task_plan": all_tasks             # Task plans generated per chunk
    }