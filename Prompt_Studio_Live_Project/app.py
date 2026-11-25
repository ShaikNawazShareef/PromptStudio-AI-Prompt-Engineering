"""
PromptStudio AI - Live Web Platform
Module 08: Prompt Engineering (Fundamentals, Few-Shot & Chain-of-Thought)
Runs on Port 8110
"""

import os
import sys
import zipfile
from typing import Optional, Dict, Any, List
from pydantic import BaseModel

from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from prompt_engine.anatomy_linter import PromptAnatomyLinter
from prompt_engine.few_shot import FewShotManager
from prompt_engine.cot_reasoning import CoTReasoningEngine
from prompt_engine.template_library import TemplateLibrary
from prompt_engine.guardrails import PromptGuardrail

app = FastAPI(
    title="PromptStudio AI",
    description="Interactive Prompt Engineering & Multi-Step Reasoning Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory=os.path.join(BASE_DIR, "templates"))

# Engine singletons
linter = PromptAnatomyLinter()
few_shot_mgr = FewShotManager()
cot_engine = CoTReasoningEngine()
template_lib = TemplateLibrary()
guardrails = PromptGuardrail()


# Request Schemas
class LintRequest(BaseModel):
    prompt: str

class OptimizeRequest(BaseModel):
    prompt: str
    framework: str = "RISEN"

class FewShotRequest(BaseModel):
    task_id: str = "sarcasm_detection"

class CoTRequest(BaseModel):
    problem_id: str = "warehouse_logistics"

class RenderTemplateRequest(BaseModel):
    template_id: str
    variables: Dict[str, str] = {}

class ScanInjectionRequest(BaseModel):
    text: str


@app.get("/", response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "app_name": "PromptStudio AI",
            "module": "08. Prompt Engineering — Fundamentals, Few-Shot & Chain-of-Thought",
            "port": 8110
        }
    )


@app.get("/api/status")
async def get_status():
    return {
        "status": "online",
        "port": 8110,
        "templates_available": len(template_lib.templates),
        "few_shot_benchmarks": len(few_shot_mgr.preset_benchmarks),
        "cot_problems": len(cot_engine.preset_problems)
    }


@app.post("/api/lint")
async def lint_prompt(req: LintRequest):
    score = linter.analyze(req.prompt)
    return score.model_dump()


@app.post("/api/optimize")
async def optimize_prompt(req: OptimizeRequest):
    return linter.optimize_prompt(req.prompt, target_framework=req.framework)


@app.post("/api/few-shot-compare")
async def compare_few_shot(req: FewShotRequest):
    try:
        return few_shot_mgr.simulate_comparison(req.task_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/cot-reason")
async def reason_cot(req: CoTRequest):
    try:
        return cot_engine.execute_reasoning_comparison(req.problem_id)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/api/templates")
async def get_templates():
    return template_lib.list_templates()


@app.post("/api/render-template")
async def render_template(req: RenderTemplateRequest):
    try:
        rendered = template_lib.render_template(req.template_id, req.variables)
        tpl = template_lib.get_template(req.template_id)
        return {
            "template_id": req.template_id,
            "title": tpl.title,
            "rendered_prompt": rendered,
            "variables_used": req.variables
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.post("/api/scan-injection")
async def scan_injection(req: ScanInjectionRequest):
    scan_res = guardrails.scan_for_injections(req.text)
    sandboxed = guardrails.sandbox_user_input(req.text)
    return {
        "scan": scan_res.model_dump(),
        "sandboxed_xml": sandboxed
    }


@app.get("/download/bundle.zip")
async def download_bundle():
    zip_path = os.path.join(os.path.dirname(BASE_DIR), "Prompt_Studio_Project_Bundle.zip")
    if not os.path.exists(zip_path):
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zip_file:
            for root, dirs, files in os.walk(BASE_DIR):
                if "__pycache__" in root or ".git" in root:
                    continue
                for file in files:
                    full_p = os.path.join(root, file)
                    rel_p = os.path.relpath(full_p, BASE_DIR)
                    zip_file.write(full_p, os.path.join("Prompt_Studio_Live_Project", rel_p))

    return FileResponse(
        zip_path,
        media_type="application/zip",
        filename="Prompt_Studio_Project_Bundle.zip"
    )


if __name__ == "__main__":
    import uvicorn
    print("Launching PromptStudio AI Live Server on http://localhost:8110")
    uvicorn.run(app, host="0.0.0.0", port=8110)
