# Company Research Agent

An AI-powered research assistant that analyzes a company using publicly available information and generates a structured business report with AI-driven insights.

The application combines web search, Retrieval-Augmented Generation (RAG), and a multi-step LangGraph workflow to produce company overviews, business analysis, challenges, AI opportunities, and executive recommendations.

---

## Features

- Company validation before research
- Multi-query web search using Tavily
- Retrieval-Augmented Generation (RAG)
- LangGraph-based AI workflow
- Parallel execution for faster report generation
- Live progress updates via FastAPI streaming
- Modern React frontend with real-time status tracking
- Structured business reports with source citations

---

## Architecture

```text
React Frontend
        │
        ▼
FastAPI Backend
        │
        ▼
LangGraph Research Agent
        │
        ├── Validator
        ├── Research
        ├── Evidence
        ├── Overview
        ├── Business
        ├── Challenges
        ├── AI Opportunities
        ├── CEO Pitch
        └── Report Composer
```

### Workflow

1. Validate the company.
2. Retrieve relevant information using multiple Tavily searches.
3. Convert search results into structured company evidence.
4. Generate different report sections using LLMs.
5. Execute independent analysis nodes in parallel.
6. Combine all outputs into a final business report.
7. Stream progress and return the completed report.

---

## Tech Stack

### Backend

- Python
- FastAPI
- LangGraph
- LangChain
- Pydantic

### AI

- NVIDIA NIM API
- Llama 3.2 Instruct
- Tavily Search API

### Frontend

- React
- Tailwind CSS
- Vite
- Lucide React

---

## Project Structure

```text
backend/
│
├── app/
│   ├── api/
│   ├── graph/
│   ├── llm/
│   ├── models/
│   ├── nodes/
│   ├── services/
│   ├── utils/
│   └── state.py
│
└── main.py

frontend/
│
├── src/
│   ├── components/
│   ├── pages/
│   ├── services/
│   ├── App.jsx
│   └── main.jsx
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/<your-username>/company-research-agent.git

cd company-research-agent
```

---

### Backend

```bash
cd backend

python -m venv venv

# Windows
venv\Scripts\activate

# Linux / macOS
source venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

---

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Environment Variables

Create a `.env` file inside the backend directory.

```env
TAVILY_API_KEY=your_tavily_key
NVIDIA_API_KEY=your_nvidia_key
```

---

## Sample Output

The generated report includes:

- Company Overview
- Business Analysis
- Business Challenges
- AI Opportunities
- Executive Recommendation (CEO Pitch)
- Source References

---

## Design Decisions

- Multi-step AI workflow using LangGraph.
- Retrieval-Augmented Generation to reduce hallucinations.
- Example-based JSON prompting with Pydantic validation.
- Parallel execution for independent report sections.
- Streaming responses for improved user experience.

---

## Future Improvements

- Export reports as PDF.
- Persistent report history.
- Authentication and user accounts.

---

## Acknowledgements

- LangGraph
- LangChain
- NVIDIA NIM
- Tavily Search
- FastAPI
- React
