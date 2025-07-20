from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .sub_agents.log_analyzer.agent import log_analyzer
from .sub_agents.context_retriever.agent import context_retriever
from .sub_agents.issue_creator.agent import issue_creator  # Optional

exception_coordinator = LlmAgent(
    name="exception_coordinator",
    model="gemini-2.5-pro",
    description="Coordinates subagents to analyze logs, retrieve context, suggest fixes, and push updates.",
    instruction="""
You assist developers in analyzing Java Spring Boot exceptions.
Follow this sequence:

1. Call `log_analyzer` agent to analyze the log and extract key info.
2. Call `context_retriever` agent to fetch relevant code snippets.
3. Call `fix_suggester` agent using the log and context to get root cause and fix.
4. Optionally call `issue_creator` to push the fix to JIRA, Confluence, and GitHub.

After each tool invocation, return:
- [Tool Name] tool reported: [Exact Result]
""",
    tools=[
        AgentTool(agent=log_analyzer),
        AgentTool(agent=context_retriever_agent),
        AgentTool(agent=issue_creator_agent),
    ]
)

root_agent = exception_coordinator
