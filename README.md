# ResearchFlow
AI-AGENT
# 🔬 ResearchFlow · Multi-Agent AI Research System

ResearchFlow is an advanced, production-grade research pipeline powered by a specialized network of cooperative AI agents. By distributing operations across multiple focused intelligence modules—searching, scraping, synthesis, and peer review—ResearchFlow transforms raw technical prompts into polished, factual, deep-dive research reports directly from your command line.

The workflow operates under a strict separation of concerns, ensuring high data fidelity, minimizing hallucinations, and generating publication-ready Markdown assets natively.

---

## 🏗️ Architectural & Workflow Overview
<img width="2914" height="1603" alt="Screenshot 2026-06-05 at 3 16 16 PM" src="https://github.com/user-attachments/assets/75a7f76f-22d4-465a-8a1f-3fc13e41ffa4" />

### Detailed Lifecycle Sequence
1. **Query Submission:** The user submits a highly technical or specific research query via the interface or core program wrapper.
2. **Intent Analysis:** The core `Research Agent` breaks down the request into discrete informational requirements.
3. **Information Gathering:** `Research Tools` invoke web search APIs, parse indices, and scrape relevant deep-page content.
4. **Data Pipeline Synthesis:** The `Pipeline` module aggregates payloads, filters noise, and ensures proper logical transitions.
5. **Report Generation & Critique:** LLM workflows structure the synthesized context into clean, markdown-formatted report frameworks before being audited by a validation loop.

---

## ✨ Features

- 🤖 **Multi-Agent Architecture:** Powered by a decentralized network of autonomous, cooperative agents.
- 🔍 **Automated Deep Research:** Native web scraping and search logic explicitly optimized for data extraction.
- 🛠 **Custom Tool Extensibility:** Modular decorator-based structure to hook in custom scrapers, database wrappers, or private APIs.
- 🔄 **Stateful Pipeline Engine:** Strict execution pipeline management separating discovery, content synthesis, and validation.
- 📄 **Rich Document Generation:** Generates comprehensive, natively readable Markdown (`.md`) structural assets.
- 🔑 **Secure Environment Layer:** Isolated credentials mapping using dotenv patterns for all underlying LLM endpoints and search aggregators.

---

FOR SETUP || RUN PROJECT (CLONE REPO)

1. Install the required project dependencies:
   pip install -r requirements.txt

2. Create a configuration file named `.env` in your root directory and supply your API credentials:
   MISTRAL_API_KEY=your_actual_api_key_here
   TAVILY_API_KEY = Your_actual_api_key_here

3. Initialize and execute the multi-agent framework directly within your terminal:
   streamlit run app.py

   
## 📂 Project Structure

```text
Research_agent/
│
├── .venv/               # Isolated Python virtual environment directory
├── .env                 # Local credential environment variables (Git-ignored)
├── agents.py            # AI agent profiles, instructions, and instantiation logic
├── app.py               # Main framework execution and UI layer
├── pipeline.py          # Core task workflow orchestration framework
├── tool.py              # External tool integrations (Search, scraping wrappers)
│
├── requirements.txt     # Pin-point dependency manifest
├── pyproject.toml       # Project metadata configurations
├── uv.lock              # Ultra-fast lockfile resolution tracking
└── README.md            # System comprehensive blueprint documentation


