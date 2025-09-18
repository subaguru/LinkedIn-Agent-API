from src.llms.gemini_llm import GeminiLLM

class PostNode:
    def __init__(self, llm: GeminiLLM):
        self.llm = llm

    def run(self, state: dict):
        topic = state.get("topic", "")
        summary = state.get("summary", "")

        prompt = f"""
        You are a professional LinkedIn content creator. 
        Write a LinkedIn post about the topic "{topic}" using the following summary:
        {summary}

        - Keep it concise and engaging
        - Make sure the post is relevant and directly tied to the topic
        - Highlight impact, opportunities, or actionable insights
        - Use a professional yet approachable tone
        - Include the topic explicitly in the post
        """
        response = self.llm.invoke(prompt)
        state["linkedin_post"] = response.content.strip()
        return state

