import os

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.messages import HumanMessage

load_dotenv()


llm = ChatGroq(model="openai/gpt-oss-20b",   api_key=os.environ.get("GROQ_API_KEY"),)

# message = HumanMessage(
#     content=[
#         {"type": "text", "text": "Describe this image in detail."},
#         {
#             "type": "image_url",
#             "image_url": {"url": "https://example.com/image.jpg"},
#         },
#     ]
# )
message = HumanMessage(
    content="Explain yourself in simple terms 2 lines"
)

response = llm.invoke([message])
# response = llm.invoke("what is your name!")
print(response.content)