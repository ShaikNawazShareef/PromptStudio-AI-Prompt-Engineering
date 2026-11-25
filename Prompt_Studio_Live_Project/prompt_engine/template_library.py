"""
Production Prompt Template Library.
Provides enterprise-grade prompt blueprints with parameter placeholders,
format guarantees, and guardrails across common LLM applications.
"""

from typing import List, Dict, Any
from pydantic import BaseModel


class PromptTemplate(BaseModel):
    id: str
    title: str
    category: str
    description: str
    framework: str
    variables: List[str]
    template_text: str
    example_variables: Dict[str, str]


class TemplateLibrary:
    def __init__(self):
        self.templates = self._load_templates()

    def _load_templates(self) -> Dict[str, PromptTemplate]:
        items = [
            PromptTemplate(
                id="strict_json_extraction",
                title="Strict JSON Entity & Schema Extractor",
                category="Information Extraction",
                description="Extracts structured entities into a valid JSON schema with negative constraints against conversational preamble.",
                framework="RISEN (Role, Instruction, Steps, End Goal, Narrowing)",
                variables=["input_text", "required_keys"],
                template_text="""### ROLE
You are an immutable data transformation pipeline with strict JSON serialization requirements.

### INSTRUCTION
Extract entities from the input payload and map them strictly to the specified schema keys.

### CONSTRAINTS
- Output ONLY a valid RFC 8259 JSON object.
- Do NOT wrap response in markdown code blocks (no ```json).
- Do NOT output preamble, conversational greetings, or notes.
- If a key value is not present in the text, use null.

### INPUT DATA
<payload>
{input_text}
</payload>

### REQUIRED SCHEMA KEYS
{required_keys}

### JSON OUTPUT:""",
                example_variables={
                    "input_text": "Acme Corp reported $42.5M in Q3 revenue with a net profit margin of 18%. CEO Alice Johnson noted customer retention was 94%.",
                    "required_keys": "[\"company_name\", \"quarter\", \"revenue_usd\", \"net_margin_pct\", \"executive\", \"retention_rate\"]"
                }
            ),
            PromptTemplate(
                id="rag_grounded_qa",
                title="Grounded RAG Q&A with Citation Enforcement",
                category="RAG & Knowledge Retrieval",
                description="Prevents hallucination by requiring direct verbatim citations from retrieved context documents.",
                framework="CLEAR (Context, Limitation, Expectation, Action, Review)",
                variables=["context_documents", "user_question"],
                template_text="""### CONTEXT
You have access ONLY to the verified source documents below. Do NOT use external pre-training knowledge.

<documents>
{context_documents}
</documents>

### LIMITATIONS & GUARDRAILS
1. Direct Grounding: Answer the question using ONLY facts stated in <documents>.
2. Negative Constraint: If the documents do not contain the answer, reply EXACTLY with:
   "I do not have sufficient information in the provided context to answer this question."
3. Citation Rule: For every factual claim made, append [Doc X] citation.

### QUESTION
{user_question}

### ANSWER:""",
                example_variables={
                    "context_documents": "[Doc 1] Company policy allows up to 20 days of paid vacation per calendar year for full-time employees.\n[Doc 2] Sick leave accumulates at 1.25 days per month and requires medical certificate if exceeding 3 consecutive days.",
                    "user_question": "Can I take 25 days of vacation if I don't use my sick leave?"
                }
            ),
            PromptTemplate(
                id="code_review_security",
                title="Code Quality & Security Vulnerability Audit",
                category="Software Engineering",
                description="Performs senior-level code review focusing on OWASP vulnerabilities, performance bottlenecks, and refactoring.",
                framework="Role-Task-Format",
                variables=["code_snippet", "language"],
                template_text="""### ROLE
You are a Principal Software Security Architect and Staff Code Reviewer.

### INSTRUCTION
Review the provided {language} code for:
1. Security vulnerabilities (OWASP Top 10, injection, buffer overflows, insecure deserialization)
2. Performance bottlenecks and time/space complexity (Big-O)
3. Idiomatic patterns and clean code principles

### INPUT CODE
```{language}
{code_snippet}
```

### OUTPUT FORMAT
Structure review in Markdown:
- **Executive Verdict**: [APPROVED / REVISE WITH CHANGES / REJECT - CRITICAL VULNERABILITY]
- **Vulnerability Findings**: Table of | Severity (Critical/High/Med/Low) | Location | Description |
- **Recommended Refactored Code**: Complete clean implementation
- **Complexity Analysis**: Before vs After""",
                example_variables={
                    "language": "python",
                    "code_snippet": "def get_user_profile(user_id):\n    query = f\"SELECT * FROM users WHERE id = '{user_id}'\"\n    return db.execute(query).fetchall()"
                }
            ),
            PromptTemplate(
                id="cot_math_logic",
                title="Chain-of-Thought Multi-Step Arithmetic & Logic",
                category="Reasoning & Problem Solving",
                description="Forces step-by-step scratchpad computation before producing the final numeric answer.",
                framework="Chain-of-Thought (CoT)",
                variables=["word_problem"],
                template_text="""### INSTRUCTION
Solve the following complex word problem.
You MUST write out your reasoning step-by-step using a scratchpad before stating the final answer.

### PROBLEM
{word_problem}

### SCRATCHPAD REASONING
Step 1 (Extract Given Constants):
Step 2 (Identify Formula / Operations):
Step 3 (Calculate Intermediate States):
Step 4 (Verify Against Edge Constraints):

### FINAL ANSWER:""",
                example_variables={
                    "word_problem": "A cloud server costs $0.08 per hour. A batch job takes 3.5 hours on 12 parallel instances. If you get a 15% volume discount, how much does the job cost in total?"
                }
            )
        ]
        return {item.id: item for item in items}

    def list_templates(self) -> List[Dict[str, Any]]:
        return [
            {
                "id": t.id,
                "title": t.title,
                "category": t.category,
                "description": t.description,
                "framework": t.framework,
                "variables": t.variables
            }
            for t in self.templates.values()
        ]

    def get_template(self, template_id: str) -> PromptTemplate:
        if template_id not in self.templates:
            raise ValueError(f"Template '{template_id}' not found.")
        return self.templates[template_id]

    def render_template(self, template_id: str, variable_values: Dict[str, str]) -> str:
        tpl = self.get_template(template_id)
        rendered = tpl.template_text
        for var in tpl.variables:
            val = variable_values.get(var, tpl.example_variables.get(var, f"[{var}]"))
            rendered = rendered.replace(f"{{{var}}}", str(val))
        return rendered
