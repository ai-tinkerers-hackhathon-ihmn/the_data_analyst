# the_data_analyst

## Backend

### Setup


We used `uv` as a package manager.
We recommend using `uv` to install the dependencies.

1. Install uv: https://docs.astral.sh/uv/getting-started/installation/
2. Install the dependencies: `uv sync`
3. Install the package locally `uv pip install -e .`
4. Run the backend: `uv run src/backend/main.py`

You shoud see `Hello, world!` printed in the console and a link to access a Gradio interface.

### Environment Variables

You will need to setup values for the environment variables as shown in the `.env.example` file.
We hardcoded connexion strings to two databases (PostgreSQL and MongoDB) hosted on Koyeb.
We share the connexion strings for the databases:

```shell
POSTGRES_DB=koyebdb
POSTGRES_USER=postgres-hack-ihmn
POSTGRES_PASSWORD=npg_LmzxGAr58Qtg
POSTGRES_HOST=ep-jolly-term-a25wr4mm.eu-central-1.pg.koyeb.app
POSTGRES_PORT=5432
MONGODB_URI=mongodb+srv://dbagent:9q4rfN13xCDSnv9D@ihmn.yf6fo.mongodb.net/?retryWrites=true&w=majority&appName=IHMN
```

(We know we shouldn't do that but for the sake of time)

Absolulety, the connextion strings should be input of our workflow.

### Multi-Agent Architecture  

- **Orchestrator Agent**: Manages workflow and delegates tasks to sub-agents.  
- **QA Query Analyzer**: Retrieves and processes data from **two databases**:  
  - **PostgreSQL** (hosted on Koyeb)  
  - **MongoDB** (hosted on Koyeb)  
- **Code Agent**:  
  - **Description**: Generates **Streamlit Python code** based on insights provided by the **Report Generator**.  
  - **Function**: Translates business insights into an interactive dashboard application.  
- **Report Generator**:  
  - **Description**: Creates **business reports** from insights provided by the **QA Query Analyzer**.  
  - **Function**: Summarizes key findings and translates data into actionable intelligence.  

### Judging Criteria  

#### ✅ Running Code: Fully Functional AI Agent  
Our system runs seamlessly with **SmolAgents** orchestrating multi-agent collaboration. The **Gradio chat interface** provides a user-friendly way to interact with the agents, and **Streamlit** enables on-the-fly dashboard deployment.  

#### 🎨 Innovation & Creativity: AI-Driven Multi-Agent System  
Unlike traditional BI tools, our solution operates as an **autonomous team of AI agents** that independently retrieve, analyze, and visualize data. This modular, agent-based design allows for **scalability and adaptability** across different domains.  

#### 🌍 Real-World Impact: Automated Insights with Zero Manual Effort  
Our multi-agent system reduces the **time and expertise required for data analytics**. Decision-makers can simply **chat with the AI**, receive **automated reports**, and deploy interactive dashboards **without coding or manual intervention**.  

#### 🤖 Alignment with the AI Agents Theme  
This project fully embraces **autonomous AI agents**, showcasing how **multiple specialized agents** can collaborate in **real-time** to enhance data-driven decision-making. The use of **LLMs, data connectivity, and generative AI** makes it a powerful example of **AI agent-based automation**.  

### Tech Stack & Tools  

- **LLMs**: Claude (Anthropic) 
- **Agents**: SmolAgents for multi-source data connectivity  
- **Interface**: Gradio (chat-based interaction)  
- **Dashboards**: Streamlit (local deployment)  
- **Cloud & Deployment**: Koyeb (for database hosting)  
- **Data Sources**: PostgreSQL, MongoDB, APIs, Google Search  

### Conclusion  
Our **multi-agent AI system** revolutionizes analytics by **automating the entire data pipeline—from retrieval to visualization—through AI-driven collaboration**. It exemplifies the power of **LLMs and AI agents** in real-world applications, making data insights **faster, smarter, and more accessible**.