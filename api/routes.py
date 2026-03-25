"""
routes.py

This module defines all API endpoints for the Requirement AI System.
It handles incoming HTTP requests, validates user input, and interacts
with the service layer to process requirements using AI models.

Responsibilities:
- Define REST API routes
- Handle request/response lifecycle
- Perform input validation
- Return structured JSON responses
"""


from fastapi import APIRouter, UploadFile, File, Form, HTTPException

from services.extractor import extract_requirements
from services.risk_analyzer import analyze_risks
from services.task_planner import plan_tasks
from services.parser import parse_pdf_upload

router = APIRouter()

# -----------------------------
# 📌 RAW TEXT ANALYSIS (API)
# -----------------------------
@router.post("/api/analyze-text")
async def analyze_text_api(text: str = Form(...)):
    try:
        requirements = extract_requirements(text)
        risks = analyze_risks(text)
        tasks = plan_tasks(requirements, risks)

        return {
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# 📌 PDF ANALYSIS (API)
# -----------------------------
@router.post("/api/analyze-pdf")
async def analyze_pdf_api(file: UploadFile = File(...)):
    try:
        pdf_text = await parse_pdf_upload(file)

        requirements = extract_requirements(pdf_text)
        risks = analyze_risks(pdf_text)
        tasks = plan_tasks(requirements, risks)

        return {
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# 🎨 UI — TEXT FORM
# -----------------------------
@router.post("/ui/analyze-text")
async def analyze_text_ui(text: str = Form(...)):
    try:
        requirements = extract_requirements(text)
        risks = analyze_risks(text)
        tasks = plan_tasks(requirements, risks)

        return {
            "status": "success",
            "source": "ui",
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------------------
# 🎨 UI — PDF UPLOAD
# -----------------------------
@router.post("/ui/analyze-pdf")
async def analyze_pdf_ui(file: UploadFile = File(...)):
    try:
        pdf_text = await parse_pdf_upload(file)

        requirements = extract_requirements(pdf_text)
        risks = analyze_risks(pdf_text)
        tasks = plan_tasks(requirements, risks)

        return {
            "status": "success",
            "source": "ui",
            "requirements": requirements,
            "risks": risks,
            "task_plan": tasks
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
