"""
pdf_reader.py

This module handles PDF text extraction for the Requirement AI System.
It provides utility functions to read and convert PDF content into
plain text for further processing in the pipeline.

Key Responsibilities:
- Extract text from PDF files using file paths
- Extract text from in-memory PDF data (bytes)
- Support file uploads via FastAPI (UploadFile)

How it works:
- Uses PyMuPDF (fitz) to open and read PDF documents
- Iterates through each page and extracts textual content
- Aggregates all page text into a single string
- Strips unnecessary whitespace for clean output

Why needed:
- Enables processing of real-world documents like requirement specs
- Supports both local file input and API-based file uploads
- Acts as the input layer for PDF-based pipeline execution

Design Considerations:
- Separate functions for file path and byte-based processing
- Async support for handling uploaded files efficiently
- Ensures compatibility with FastAPI request handling

Limitations:
- Extracts only text (no images or tables processing)
- Accuracy depends on PDF structure and formatting
"""

import fitz  # PyMuPDF
from io import BytesIO
from fastapi import UploadFile


def extract_text_from_pdf_path(file_path: str) -> str:
    """Extracts text from a PDF given a file path"""
    text = ""

    with fitz.open(file_path) as doc:
        for page in doc:
            text += page.get_text()

    return text.strip()


def extract_text_from_pdf_bytes(pdf_bytes: bytes) -> str:
    """Extracts text from uploaded PDF bytes"""
    text = ""

    with fitz.open(stream=pdf_bytes, filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()

    return text.strip()


async def parse_pdf_upload(file: UploadFile) -> str:
    """Reads UploadFile and extracts text"""
    pdf_bytes = await file.read()
    return extract_text_from_pdf_bytes(pdf_bytes)
