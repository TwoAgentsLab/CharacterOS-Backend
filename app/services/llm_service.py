import logging
from langchain_groq import ChatGroq
from app.config.config import GROQ_API_KEY

logger = logging.getLogger(__name__)

class LLMBrain:
    def __init__(self, model_name: str = "llama-3.1-8b-instant", temperature: float = 0.35, max_tokens: int = 900):
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        
        # Initializing Groq Chat
        self._llm = ChatGroq(
            api_key = GROQ_API_KEY,
            model = model_name,
            temperature = temperature,
            max_tokens = max_tokens
        )
        
    def invoke_llm(self, messages):
        return self._llm.invoke(messages)