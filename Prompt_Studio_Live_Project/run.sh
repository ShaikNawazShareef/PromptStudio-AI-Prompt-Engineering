#!/usr/bin/env bash
# PromptStudio AI Launcher
# Module 08: Prompt Engineering - Fundamentals, Few-Shot & Chain-of-Thought
# Runs on Port 8110

set -e

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd "$DIR"

PYTHON_BIN="/home/hemanth/jupyterenv/bin/python"
if [ ! -f "$PYTHON_BIN" ]; then
    PYTHON_BIN="python3"
fi

echo "======================================================================"
echo "          PROMPTSTUDIO AI - PROMPT ENGINEERING HUB (PORT 8110)"
echo "======================================================================"
echo "Using Python: $PYTHON_BIN"

BUNDLE_ZIP="../Prompt_Studio_Project_Bundle.zip"
if [ ! -f "$BUNDLE_ZIP" ]; then
    echo "Creating project standalone bundle ZIP..."
    (cd .. && zip -rq "Prompt_Studio_Project_Bundle.zip" "Prompt_Studio_Live_Project" -x "*/__pycache__/*" "*/.git/*")
fi

echo "Starting PromptStudio AI server on http://localhost:8110 ..."
$PYTHON_BIN -m uvicorn app:app --host 0.0.0.0 --port 8110 --reload
