from json import load

from langchain.chat_models import BaseChatModel, init_chat_model
from dotenv import load_dotenv

load_dotenv()

def load_llm() -> BaseChatModel:
    return init_chat_model("groq:openai/gpt-oss-120b")
