from src.llms.gemini_llm import GeminiLLM
import re

class ImageNode:
    def __init__(self, llm: GeminiLLM):
        self.llm = llm

    def run(self, state: dict):
        topic = state.get("topic", "")

        prompt = f"""
        Suggest a royalty-free image URL for a LinkedIn post about: "{topic}".
        Prefer Unsplash or Pexels URLs. If no URL is available, return "None".
        Only return a single URL or "None".
        """

        response = self.llm.invoke(prompt)
        content = response.content.strip()

        url_pattern = r'(https?://[^\s]+)'
        match = re.search(url_pattern, content)
        image_url = match.group(0) if match else None

        state["image_suggestion"] = image_url
        return state

