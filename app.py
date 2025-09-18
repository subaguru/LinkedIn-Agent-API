import uvicorn
from fastapi import FastAPI, Request
from src.graphs.graph_builder import GraphBuilder
from src.llms.gemini_llm import GeminiLLM
from src.states.linkedin_state import BlogRequest,LinkedInPost
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI(title="LinkedIn Agent API",
    description="Generate LinkedIn posts using Gemini and Tavily search",
    version="1.0.0",
    docs_url="/docs",   
    redoc_url="/redoc")

@app.post("/generate-post", response_model=LinkedInPost)
async def create_blogs(request: BlogRequest):
    topic = request.topic

    if not topic:
        return {"error": "No topic provided"}

    
    gemini_llm = GeminiLLM()
    llm = gemini_llm.get_llm()

    
    graph_builder = GraphBuilder(llm)
    graph = graph_builder.build_graph()

    
    initial_state = {"topic": topic}
    state = graph.invoke(initial_state)

    return {
        "topic": state.get("topic"),
        "linkedin_post": state.get("linkedin_post"),
        "news_sources": state.get("news_sources", []),
        "image_suggestion": state.get("image_suggestion"),
    }

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True, reload_dirs=["./src"])

