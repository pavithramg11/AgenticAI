from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime


search = DuckDuckGoSearchRun()


@tool
def search_tool(query: str) -> str:
    """Search the web for current information."""
    return search.run(query)