from tavily import TavilyClient
import os
import time

class SearchNode:
    def __init__(self):
        self.max_retries = 3
        api_key = os.getenv("TAVILY_API_KEY")
        if not api_key:
            raise ValueError("TAVILY_API_KEY not found in environment variables.")
        self.client = TavilyClient(api_key=api_key)

    def run(self, state: dict):
        topic = state.get("topic", "")
        results = []

        if not topic:
            return {**state, "news_sources": ["No topic provided"]}

        for attempt in range(1, self.max_retries + 1):
            try:
                
                response = self.client.search(query=topic)
                results = [item.get("url") for item in response.get("results", []) if item.get("url")]

                if results:
                    break  
                else:
                    print(f"Attempt {attempt}: No results returned, retrying...")
                    time.sleep(1)

            except Exception as e:
                print(f"Attempt {attempt} failed with error: {e}")
                time.sleep(1)

        if not results:
            results = ["No results found or search failed"]

        return {**state, "news_sources": results[:3]}