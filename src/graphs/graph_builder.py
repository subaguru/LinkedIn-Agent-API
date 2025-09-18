from langgraph.graph import StateGraph, START, END
from src.states.linkedin_state import LinkedInState
from src.nodes.search_node import SearchNode
from src.nodes.summarize_node import SummarizeNode
from src.nodes.post_node import PostNode
from src.nodes.image_node import ImageNode

class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(LinkedInState)

    def build_graph(self):
        search_node = SearchNode()
        summarize_node = SummarizeNode(self.llm)
        post_node = PostNode(self.llm)
        image_node = ImageNode(self.llm)

        # Add nodes
        self.graph.add_node("search", search_node.run)
        self.graph.add_node("summarize", summarize_node.run)
        self.graph.add_node("post", post_node.run)
        self.graph.add_node("image", image_node.run)

        # Define edges
        self.graph.add_edge(START, "search")
        self.graph.add_edge("search", "summarize")
        self.graph.add_edge("summarize", "post")
        self.graph.add_edge("post", "image")
        self.graph.add_edge("image", END)

        return self.graph.compile()



