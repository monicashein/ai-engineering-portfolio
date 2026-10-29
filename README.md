# Enterprise Data to AI Engineering Portfolio

## Introduction
* **Who:** An enterprise data architect and solutions builder with over 20 years of experience specializing in utility sector infrastructure, big data warehouses, and complex data pipelines.
* **What:** This repository serves as my structured roadmap and hands-on codebase for transitioning into a Senior/Lead AI Engineer, bridging large-scale data architecture with intelligent LLM applications.
* **Roadmap:**
  * **M1:** CLI chatbot 
  * **M2:** Agent with tools 
  * **M3:** RAG + MCP 
  * **M4:** Multi-agent with human approval 
  * **M5:** Production on Azure

## Setup Instructions

Follow these steps to set up and run this project locally:

1. Clone the repository
   ```bash
   git clone git@github.com:monicashein/ai-engineering-portfolio.git
   cd ai-engineering-portfolio
   ```
2. Create and activate a virtual environment (Python 3.13)
   ```bash
   python3.13 -m venv .venv
   source .venv/bin/activate
   ```
3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
4. Configure secrets: copy the template, then add your own API key and model ID to `.env` (never commit `.env`)
   ```bash
   cp .env.example .env
   ```
5. Verify the setup
   ```bash
   python check_env.py
   ```