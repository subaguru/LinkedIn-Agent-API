## LinkedIn Agent API

A FastAPI-based service that generates professional LinkedIn posts using Gemini LLM and Tavily search.
It automatically finds relevant news sources, creates engaging posts, and suggests an image.

### Features
- Fetch supporting sources using Tavily search
- Generate LinkedIn-ready posts from a given topic
- Suggest a relevant image if available
- Expose REST API with Swagger UI for testing

### Setup Instructions
1. Clone the repository
    - git clone https://github.com/subaguru/LinkedIn-Agent-API.git
    - cd LINKEDIN_AGENT

2. Create and activate virtual environment
    - python -m venv .venv
    - .venv\Scripts\activate

3. Install dependencies
    - pip install -r requirements.txt

4. Add environment variables
    - GOOGLE_API_KEY = your_gemini_api_key_here
    - TAVILY_API_KEY = your_tavily_api_key_here

5. Run the server
    - uvicorn app:app --host 0.0.0.0 --port 8000 --reload

### API Documentation

### Swagger UI
- http://localhost:8000/docs

### Endpoint
- POST /generate-post

### Request Body
{
  "topic": "Artificial Intelligence"
}

### Response
{
  "topic": "Artificial Intelligence",
  "linkedin_post": "**The Future of Work: Harnessing the Power of Artificial Intelligence**\n\nAs AI...",
  "news_sources": [
    "https://en.wikipedia.org/wiki/Artificial_intelligence",
    "https://en.wikipedia.org/wiki/A.I._Artificial_Intelligence",
    "https://cloud.google.com/learn/what-is-artificial-intelligence"
  ],
  "image_suggestion": "https://www.pexels.com/photo/person-looking-at-code-on-computer-screen-1238971/"
}

### Tech Stack
- FastAPI – REST API framework
- LangChain / LangGraph – Orchestration
- Gemini LLM (Google Generative AI) – Text generation
- Tavily – Search for sources
