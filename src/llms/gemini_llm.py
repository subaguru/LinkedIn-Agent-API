from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

class GeminiLLM:
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        load_dotenv()
        self.api_key = os.getenv("GOOGLE_API_KEY")  
        if not self.api_key:
            raise ValueError("GOOGLE_API_KEY not found in environment variables")

        self.model_name = model_name
        
        self.llm = ChatGoogleGenerativeAI(
            model=self.model_name,
            api_key=self.api_key,
            temperature=0.7
        )

    def get_llm(self):
        return self.llm
