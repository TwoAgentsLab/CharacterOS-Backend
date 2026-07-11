from langgraph.graph import (
    StateGraph,
    START,
    END
)

from app.schemas.states import NPCState
from app.nodes.load_npc import load_npc_node
from app.nodes.build_prompt import build_prompt_node
from app.nodes.llm import llm_node

def build_graph():
    try:
        graph = StateGraph(NPCState)
        
        graph.add_node("load_npc", load_npc_node)
        graph.add_node("build_prompt", build_prompt_node)
        graph.add_node("llm", llm_node)
        
        graph.add_edge(START, "load_npc")
        graph.add_edge("load_npc", "build_prompt")
        graph.add_edge("build_prompt", "llm")
        graph.add_edge("llm", END)
        
        return graph.compile()
    except Exception as e:
        print(f"Error building graph: {e}")
        raise
        