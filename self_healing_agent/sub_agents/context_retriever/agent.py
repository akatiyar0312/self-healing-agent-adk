from google.adk.agents import LlmAgent
from langchain_core.tools import tool
from .prompt import CONTEXT_RETRIEVER_PROMPT

@tool
def get_context(log: str):
    """
    Retrieves relevant source code context for a given Java exception log.
    
    Args:
        log (str): The exception or error log from a Java application.

    Returns:
        List[Document]: Relevant source code snippets or documentation.
    """
    from agents.shared_retriever import retriever
    return retriever.get_relevant_documents(log)

context_retriever = LlmAgent(
    name="context_retriever",
    model="gemini-2.5-pro",
    description="Fetches relevant Java source context for a given exception.",
    instruction=CONTEXT_RETRIEVER_PROMPT,
    tools=[get_context]
)
