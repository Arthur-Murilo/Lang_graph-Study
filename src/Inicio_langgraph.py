from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.7,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

messages = [
    (
        "system",
        "Você é um assistente bem legal por sinal",
    ),
    ("human", "Opa tudo bem, em respodne em portugues tá?"),
]
ai_msg = model.invoke(messages)
print(ai_msg.content)