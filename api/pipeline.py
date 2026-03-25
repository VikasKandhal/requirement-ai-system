"""
pipeline.py

Central orchestration module that coordinates multiple services to process
user input (either plain text or PDF) and generate structured outputs.

This pipeline ensures modular processing by delegating tasks like:
- Requirement extraction
- Risk analysis
- Task planning

It supports scalability via chunk-based processing for large inputs.
"""

# Import core service modules for different processing stages
from services.extractor import extract_requirements   # Extract structured requirements from text
from services.risk_analyzer import analyze_risks      # Analyze potential risks from input
from services.task_planner import plan_tasks          # Generate task plan based on requirements & risks

# Import utilities for handling PDF inputs and large text
from services.pdf_reader import read_pdf_text         # Reads and extracts text from PDF files
from services.chunker import chunk_text               # Splits large text into smaller chunks


def run_pipeline(text: str = None, pdf_path: str = None):
    """
    Unified orchestrator for:
    - plain text input
    - pdf input (chunked)
    """

    # Step 1: Handle input source (PDF or plain text)
    # If PDF path is provided, extract full text and split into chunks
    if pdf_path:
        full_text = read_pdf_text(pdf_path)   # Extract text content from PDF
        chunks = chunk_text(full_text)        # Divide text into manageable chunks
    else:
        # If plain text is provided, wrap it into a list for uniform processing
        chunks = [text]

    # Step 2: Initialize containers to store aggregated outputs
    all_requirements = []   # Stores extracted requirements for each chunk
    all_risks = []          # Stores identified risks for each chunk
    all_tasks = []          # Stores generated task plans for each chunk

    # Step 3: Process each chunk independently
    # This improves scalability and handles large inputs efficiently
    for chunk in chunks:

        # Extract requirements from the current chunk
        req = extract_requirements(chunk)

        # Analyze risks associated with the chunk
        risk = analyze_risks(chunk)

        # Generate task plan based on extracted requirements and risks
        task = plan_tasks(req, risk)

        # Append results to respective lists for aggregation
        all_requirements.append(req)
        all_risks.append(risk)
        all_tasks.append(task)

    # Step 4: Return final aggregated output
    return {
        "chunks_processed": len(chunks),  # Total number of processed chunks
        "requirements": all_requirements, # List of requirements for each chunk
        "risks": all_risks,               # List of risks for each chunk
        "task_plan": all_tasks            # List of task plans for each chunk
    }