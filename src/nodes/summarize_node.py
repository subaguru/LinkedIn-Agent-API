from src.llms.gemini_llm import GeminiLLM

class SummarizeNode:
    def __init__(self, llm: GeminiLLM):
        self.llm = llm

    def run(self, state: dict):
        topic = state.get("topic", "")
        sources = state.get("news_sources", [])

        prompt = f"""
        You are a professional summarizer. Summarize the key insights about the topic: "{topic}" 
        using ONLY the following sources:
        {sources}

        - Be concise and factual
        - Ensure all information is accurate and directly related to the topic
        - The output should be suitable for creating a LinkedIn post
        """
        response = self.llm.invoke(prompt)
        state["summary"] = response.content.strip()  
        return state


