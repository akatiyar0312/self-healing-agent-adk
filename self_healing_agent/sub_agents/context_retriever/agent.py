from google.adk.agents import ToolAgent
from langchain_core.tools import tool
from .prompt import CONTEXT_RETRIEVER_PROMPT

@tool
def get_context(log: str):
    from agents.shared_retriever import retriever
    return retriever.get_relevant_documents(log)

context_retriever = ToolAgent(
    name="context_retriever",
    model="gemini-2.5-pro",
    description="Fetches relevant Java source context for a given exception.",
    instruction=CONTEXT_RETRIEVER_PROMPT,
    tools=[get_context]
)
