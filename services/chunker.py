"""
chunker.py

This module provides functionality to split large text into smaller,
manageable chunks for efficient processing by AI models.

Key Responsibilities:
- Break long input text into fixed-size segments
- Introduce overlap between chunks to preserve context
- Enable processing of large documents without losing continuity

How it works:
- The text is divided into chunks of a specified maximum size
- A fixed overlap is maintained between consecutive chunks
- This overlap ensures that important information at boundaries
  is not lost during chunk-wise processing

Why needed:
- Many AI/LLM models have input size limitations
- Chunking allows scalable processing of large inputs like PDFs
- Overlapping improves accuracy by maintaining context across chunks
"""

def chunk_text(text: str, max_chars: int = 4000):
    """
    Splits text into overlapping chunks to avoid context loss.
    """

    chunks = []
    start = 0
    overlap = 400

    while start < len(text):
        end = start + max_chars
        chunk = text[start:end]

        chunks.append(chunk)
        start = end - overlap

    return chunks
