"""
pdf_parser.py

This module provides a lightweight and safe method for extracting text
from PDF files using byte streams.

Key Responsibilities:
- Convert PDF byte data into readable plain text
- Handle PDF parsing without relying on OCR tools like Tesseract
- Clean extracted text to remove unwanted or corrupted characters

How it works:
- Uses PyPDF2 to read PDF content from an in-memory byte stream
- Iterates through each page and extracts textual content
- Handles cases where pages may return empty or None text
- Cleans common Unicode artifacts for better downstream processing

Why needed:
- Enables efficient processing of uploaded PDF files in APIs
- Avoids heavy dependencies like OCR when text is already embedded
- Provides a reliable fallback mechanism for structured text extraction

Design Considerations:
- Uses try-except block for robust error handling
- Returns empty string instead of crashing on failure
- Applies basic text cleaning to improve data quality

Limitations:
- Does not support scanned/image-based PDFs (no OCR)
- Extraction quality depends on PDF encoding and structure
"""

from io import BytesIO
from PyPDF2 import PdfReader


def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    """
    Safely extract text from a PDF byte stream
    without requiring Tesseract or OCR.
    """

    text = ""

    try:
        reader = PdfReader(BytesIO(pdf_bytes))

        for page in reader.pages:
            page_text = page.extract_text() or ""
            text += page_text + "\n"

    except Exception as e:
        print("PDF parsing error:", e)
        return ""

    # Clean weird unicode artifacts sometimes seen in PDFs
    text = (
        text.replace("\x00", "")
            .replace("\u200b", "")
            .replace("cid:", "")
            .strip()
    )

    return text
