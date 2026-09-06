from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.prompts import ChatPromptTemplate
from tools import search_tool

load_dotenv()


class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]


llm = ChatOpenAI(model="gpt-4o-mini")

tools = [search_tool]

prompt = """You are a research assistant.

Use the available tools when needed.
Do not invent sources.

Return the final answer in the required structured format
            """

agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=prompt,
    response_format=ResearchResponse,

)

query = input("Enter your research query: ").strip()
result = agent.invoke({"query": query})
print(result)



