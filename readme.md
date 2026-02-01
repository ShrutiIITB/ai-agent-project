
# AI Agent Project

## Overview
This project implements a multi-agent AI interface with web search, where user can choose any OpenAI model and query

## Features
- App utilises LangChain, FastAPI, Streamlit, OpenAI and Tavilly
- Created CI/CD pipeline using Git, Jenkins, SonarQube

### Project Map
<p align="left">
  <img src="img\architecture.jpeg" width=400/>
</p>



## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup
1. Clone the repository
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. Configure your openai and tavilly key environment variables in `.env` file



## Project Structure
```
ai-agent/
├── src/
│   ├── agent/
│   ├── backend/
│   ├── frontend/
│   ├── utils/
│   └── config/
├── custom_jenkins/
├── requirements.txt
├── Dockerfile
├── Jenkinsfile
└── readme.md
```


## Testing
```bash
python -m app.app
```

