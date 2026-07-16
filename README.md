# ResearchFlow
AI-AGENT
# 🔬 ResearchFlow · Multi-Agent AI Research System

ResearchFlow is an advanced, production-grade research pipeline powered by a specialized network of cooperative AI agents. By distributing operations across multiple focused intelligence modules—searching, scraping, synthesis, and peer review—ResearchFlow transforms raw technical prompts into polished, factual, deep-dive research reports directly from your command line. 
The workflow operates under a strict separation of concerns, ensuring high data fidelity, minimizing hallucinations, and generating publication-ready Markdown assets natively. Its modular, scalable architecture enables reliable, high-quality research automation for complex technical and scientific domains.

-----------------------------------------------------------------------------------------------

## 🏗️ Architectural & Workflow Overview

=======
<img width="2914" height="1603" alt="Screenshot 2026-06-05 at 3 16 16 PM" src="https://github.com/user-attachments/assets/75a7f76f-22d4-465a-8a1f-3fc13e41ffa4" />


https://github.com/user-attachments/assets/d3695153-f7c0-407f-8d23-fa36df8b9df2




### Detailed Lifecycle Sequence
1. **Query Submission:** The user submits a highly technical or specific research query via the interface or core program wrapper.
2. **Intent Analysis:** The core `Research Agent` breaks down the request into discrete informational requirements.
3. **Information Gathering:** `Research Tools` invoke web search APIs, parse indices, and scrape relevant deep-page content.
4. **Data Pipeline Synthesis:** The `Pipeline` module aggregates payloads, filters noise, and ensures proper logical transitions.
5. **Report Generation & Critique:** LLM workflows structure the synthesized context into clean, markdown-formatted report frameworks before being audited by a validation loop.

---

## Features

- 🔍 Multi-agent orchestration via LangGraph
- 🔐 User authentication (signup/login) with bcrypt password hashing
- 📄 Live pipeline status tracking in the UI
- 📝 Markdown report export
- 🧐 Automated critic feedback on generated reports
- 🎨 Custom-styled Streamlit interface

---

## Tech Stack
- **Frontend/UI:** Streamlit
- **Orchestration:** LangChain, LangGraph
- **LLM:** Mistral AI
- **Search:** Tavily API
- **Auth:** bcrypt password hashing, SQLAlchemy ORM
- **Database:** SQLite (dev) / PostgreSQL-ready
- **Package management:** uv

--------
## Setup

1. **Clone the repo**
```bash
   git clone https://github.com/krishna231122-del/Research_agent.git
   cd Research_agent
```

2. **Create a virtual environment and install dependencies**
```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
```

3. **Set up environment variables** — create a `.env` file:
   
## 📂 Project Structure
```text
Research_agent/
├── app.py                 # Main Streamlit app + auth gate + pipeline UI
├── agents.py               # Agent definitions (search, reader, writer, critic)
├── pipeline.py             # Core pipeline orchestration logic
├── tool.py                 # External tool integrations (search, scraping)
├── Database1.py            # SQLAlchemy engine, session, Base
├── init_db.py               # One-time script to create DB tables
├── auth/
│   ├── models.py           # User table (SQLAlchemy model)
│   ├── security.py         # Password hashing (bcrypt)
│   └── service.py          # create_user, authenticate_user logic
├── requirements.txt
├── pyproject.toml
└── uv.lock
```text
4. **Initialize the database**
```bash
   python3 init_db.py
```

5. **Run the app**
```bash
   streamlit run app.py
```

6. Open `http://localhost:8501` in your browser, sign up, and start researching.

## How It Works

1. User signs up / logs in (credentials hashed with bcrypt, stored in SQLite via SQLAlchemy)
2. User enters a research topic
3. The pipeline runs sequentially through all four agents, streaming progress to the UI
4. Final report and critic feedback are displayed, with a downloadable `.md` export

## Roadmap

- [ ] JWT-based API layer for programmatic access
- [ ] Per-user research history
- [ ] Rate limiting per user
- [ ] PostgreSQL deployment support

## License

MIT
