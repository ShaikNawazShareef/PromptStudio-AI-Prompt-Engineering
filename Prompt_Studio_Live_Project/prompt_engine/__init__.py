"""
Prompt Engineering Core Package.
Provides modules for:
- Prompt Anatomy Analysis & Linter
- Few-Shot & In-Context Exemplar Learning
- Chain-of-Thought (CoT) & Self-Consistency Reasoning
- Production Prompt Templates
- Defensive Prompt Guardrails
"""

from .anatomy_linter import PromptAnatomyLinter, PromptScore
from .few_shot import FewShotManager, Exemplar
from .cot_reasoning import CoTReasoningEngine, ReasoningResult
from .template_library import TemplateLibrary
from .guardrails import PromptGuardrail

__all__ = [
    "PromptAnatomyLinter",
    "PromptScore",
    "FewShotManager",
    "Exemplar",
    "CoTReasoningEngine",
    "ReasoningResult",
    "TemplateLibrary",
    "PromptGuardrail",
]
