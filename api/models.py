"""
schemas.py

This module defines the data models (schemas) used for request validation
and response formatting in the Requirement AI System.

Pydantic models ensure:
- Type validation
- Data consistency
- Automatic request parsing in FastAPI
"""

# Import BaseModel from Pydantic for data validation and parsing
from pydantic import BaseModel

# Import typing utilities for better type annotations
from typing import Any, Dict


# Request schema for incoming user input
# This model validates the structure of the request body
class RequirementRequest(BaseModel):
    text: str   # Raw user input containing requirements


# Response schema for pipeline output
# Defines the structure of the API response returned to the client
class PipelineResponse(BaseModel):
    requirements: dict   # Structured requirements extracted from input
    risks: dict          # Identified risks associated with requirements
    task_plan: dict      # Generated task plan based on requirements and risks