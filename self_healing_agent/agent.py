# agents/main_agent.py

from google.adk.agents import LlmAgent
from google.adk.tools.agent_tool import AgentTool

from .log_analyzer.agent import log_analyzer_agent
from .context_retriever.agent import context_retriever_agent
from .fix_suggester.agent import fix_suggester_agent
from .issue_creator.agent import issue_creator_agent
from .prompt import exception_coordinator_prompt  # <-- 🆕 import prompt

exception_coordinator = LlmAgent(
    name="exception_coordinator",
    model="gemini-2.5-pro",
    description="Coordinates subagents to analyze logs, retrieve context, suggest fixes, and push updates.",
    instruction=exception_coordinator_prompt,
    tools=[
        AgentTool(agent=log_analyzer_agent),
        AgentTool(agent=context_retriever_agent),
        AgentTool(agent=fix_suggester_agent),
        AgentTool(agent=issue_creator_agent),
    ]
)

root_agent = exception_coordinator
