# 🚀 PromptStudio-AI
### Craft Better Prompts. Engineer Smarter AI.

PromptStudio-AI is an interactive Prompt Engineering platform built using **Python and FastAPI**. It helps analyze, optimize, compare, and improve prompts using different prompt engineering techniques.

The platform demonstrates prompt fundamentals, Few-Shot Learning, Chain-of-Thought reasoning, Self-Consistency, and defensive prompting with security guardrails.

## ✨ Features

- 🧠 **Prompt Anatomy Linter** – Analyzes prompt quality and provides reliability scores.
- ⚡ **Prompt Optimizer** – Automatically improves prompts using the RISEN framework.
- 🎯 **Few-Shot Learning** – Compares Zero-Shot, One-Shot, and Few-Shot prompting.
- 🔍 **Chain-of-Thought Reasoning** – Demonstrates multi-step reasoning comparisons.
- 🔄 **Self-Consistency** – Evaluates multiple reasoning paths and consensus.
- 📚 **Prompt Template Library** – Provides reusable prompt templates.
- 🛡️ **Prompt Injection Scanner** – Detects potentially malicious instructions and applies security guardrails.
- 🌐 **Interactive Web Dashboard** – Access prompt engineering features through a FastAPI-powered interface.
- 💻 **CLI Interface** – Run demonstrations directly from the terminal.

## 🛠️ Technologies Used

- Python
- FastAPI
- Pydantic
- Uvicorn
- HTML
- CSS
- JavaScript

## 📂 Project Structure

```text
PromptForge-AI/
│
├── app.py
├── demo_cli.py
│
├── prompt_engine/
│   ├── anatomy_linter.py
│   ├── few_shot.py
│   ├── cot_reasoning.py
│   ├── template_library.py
│   └── guardrails.py
│
├── templates/
├── static/
│
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/PromptForge-AI.git
```

**2. Navigate to the project directory**

```bash
cd PromptForge-AI
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

## ▶️ Usage

### Run the Web Application

```bash
python app.py
```

Open your browser:

```text
http://localhost:8110
```

### Run the CLI Application

```bash
python demo_cli.py
```

Run all demonstrations:

```bash
python demo_cli.py --all
```

## 🔗 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Web dashboard |
| GET | `/api/status` | Application status |
| POST | `/api/lint` | Analyze prompts |
| POST | `/api/optimize` | Optimize prompts |
| POST | `/api/few-shot-compare` | Compare prompting methods |
| POST | `/api/cot-reason` | Reasoning comparison |
| GET | `/api/templates` | List prompt templates |
| POST | `/api/render-template` | Render a template |
| POST | `/api/scan-injection` | Scan prompt injection |
| GET | `/download/bundle.zip` | Download project bundle |

## 📸 Screenshots

Add your project dashboard screenshots here.

```markdown
![PromptForge-AI Dashboard](screenshots/dashboard.png)
```

## 🎯 Learning Objectives

- Understand prompt engineering fundamentals.
- Explore different prompting strategies.
- Learn prompt optimization techniques.
- Understand multi-step reasoning comparisons.
- Explore prompt injection detection and defensive prompting.
- Build interactive AI-focused applications using FastAPI.

## 🔮 Future Improvements

- Integration with LLM APIs.
- Support for additional prompt frameworks.
- Advanced prompt evaluation benchmarks.
- Prompt history and management.
- User authentication.
- Cloud deployment.

## 👨‍💻 Author

**Shaik Nawaz Shareef**

GitHub: https://github.com/ShaikNawazShareef

## ⭐ Support

If you find this project useful, consider giving it a star ⭐ on GitHub.

---

**PromptForge-AI – Craft Better Prompts. Engineer Smarter AI.**
