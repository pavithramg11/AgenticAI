from langgraph.graph import StateGraph, START, END
from langchain_groq import ChatGroq
from typing import TypedDict, Annotated, Literal
from langchain_core.messages import BaseMessage, HumanMessage
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import MemorySaver

from dotenv import load_dotenv
import operator

load_dotenv()

llm =  ChatGroq(
    model="openai/gpt-oss-120b")

class ChatState(TypedDict):

    messages: Annotated[list[BaseMessage], add_messages]

def chat_node(state: ChatState):
    messages=state['messages']
    response=llm.invoke(messages)
    return {'messages':[response]}


checkpoint = MemorySaver()

graph = StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node',END)

chatbot = graph.compile(checkpointer=checkpoint)