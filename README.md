# Multi-Agent Research Assistant

This project is an AI-powered research assistant that automates the process of gathering, analyzing, and compiling information on any given topic. It leverages a multi-agent architecture where specialized AI agents collaborate to perform a research task from start to finish.

## Features

- **Automated Research Pipeline**: From a single topic, the system automatically searches the web, reads relevant sources, drafts a report, and provides a critique.
- **Multi-Agent System**: Utilizes a team of AI agents, each with a specific role:
    - **Search Agent**: Gathers up-to-date information from the web.
    - **Reader Agent**: Scrapes and extracts content from URLs.
    - **Writer Agent**: Composes a structured and detailed research report.
    - **Critic Agent**: Evaluates the report for quality and provides feedback.
- **Powered by Cutting-Edge LLMs**: Integrates powerful language models like Llama 3 (via Groq) and Mistral for high-quality content generation and analysis.
- **Extensible Toolset**: Built with LangChain, allowing for easy integration of new tools and agents.

## How It Works

The research process is orchestrated as a sequential pipeline:

1.  **Search**: The user provides a research topic. The **Search Agent** uses the Tavily API to find relevant articles and sources on the web.
2.  **Read**: The **Reader Agent** selects the most promising URL from the search results and scrapes its content to gather in-depth information.
3.  **Write**: The **Writer Agent** receives the search results and the scraped content. It then synthesizes this information into a coherent and structured research report, including an introduction, key findings, a conclusion, and a list of sources.
4.  **Critique**: The **Critic Agent** reviews the generated report, provides a score out of 10, and offers constructive feedback on its strengths and areas for improvement.

## Technologies Used

-   **Backend**: Python
-   **AI & LLMs**:
    -   [LangChain](https://www.langchain.com/) for agent and chain orchestration.
    -   [Groq](https://groq.com/) for high-speed Llama 3 inference.
    -   [Mistral AI](https://mistral.ai/) for alternative model endpoints.
-   **Tools**:
    -   [Tavily](https://tavily.com/) for the web search API.
    -   [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for web scraping.

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-folder>
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up environment variables:**
    Create a file named `.env` in the root of the project and add your API keys:
    ```
    TAVILY_API_KEY="your_tavily_api_key"
    GROQ_API_KEY="your_groq_api_key"
    MISTRAL_API_KEY="your_mistral_api_key"
    ```

## Usage

To run the research pipeline, execute the `pipeline.py` script:

```bash
python pipeline.py
```

The script will prompt you to enter a research topic. The agents will then carry out the research process, and you will see the output printed to the console.

## Project Structure

```
.
├── agents.py               # Defines the AI agents and chains
├── pipeline.py             # Main script to run the research pipeline
├── tools.py                # Contains custom tools (web search, scraping)
├── requirements.txt        # Project dependencies
├── README.md               # This file
└── .env                    # For API keys (not included in repo)
```
