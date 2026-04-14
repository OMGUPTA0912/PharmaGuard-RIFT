from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from typing import List
import uuid
from datetime import datetime, timezone
import json

from services.vcf_parser import parse_vcf
from services.risk_engine import evaluate_risks

app = FastAPI(title="PharmaGuard API")

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")

# Configure CORS for local React app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/api/analyze")
async def analyze_vcf(file: UploadFile = File(...), drugs: str = Form(...)):
    # 1. Validate File Size/Type
    if not (file.filename.endswith(".vcf") or file.filename.endswith(".vcf.gz")):
        raise HTTPException(status_code=400, detail="Invalid file type. Must be .vcf or .vcf.gz.")
    
    file_contents = await file.read()
    if len(file_contents) > 5 * 1024 * 1024:
        raise HTTPException(status_code=400, detail="File size exceeds 5MB limit.")
        
    try:
        medications = json.loads(drugs)
        if not isinstance(medications, list):
            raise ValueError()
    except:
        # Fallback to comma separation
        medications = [d.strip() for d in drugs.split(",") if d.strip()]

    # 2. Parse genomic data for target variants using regex heuristic
    genetic_profile = parse_vcf(file_contents, file.filename)
    
    # 3. Evaluate clinical risks and generate CPIC insights / LLM mock
    result_payload = evaluate_risks(genetic_profile, medications)
    
    # 4. Apply universally required metadata fields
    result_payload["patient_id"] = str(uuid.uuid4())
    result_payload["timestamp"] = datetime.now(timezone.utc).isoformat()
    result_payload["quality_metrics"]["file_size_bytes"] = len(file_contents)

    return result_payload
