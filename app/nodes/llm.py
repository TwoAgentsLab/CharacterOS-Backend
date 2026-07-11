from app.schemas.states import NPCState
from app.services.llm_service import LLMBrain

llm = LLMBrain()

def llm_node(state: NPCState):
    try:
        data = state["prompt"]
        response = llm.invoke_llm(data)
        return {
            "response": response.content
        }
    except Exception as e:
        print(f"Error in LLM node: {e}")