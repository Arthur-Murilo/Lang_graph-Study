from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.7,  # Gemini 3.0+ defaults to 1.0
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
    ("human", "OPa tudo bem, em respodne em portugues tá?"),
]
ai_msg = model.invoke(messages)
print(ai_msg.content)