from google.adk.agents import LlmAgent
from google.adk.tools.mcp_tool import MCPToolset, StreamableHTTPConnectionParams
from .prompt import ISSUE_CREATOR_PROMPT
import os

mcp_tools = MCPToolset(
    connection_params=StreamableHTTPConnectionParams(
        url=os.getenv("MCP_TOOLBOX_URL"),
        headers={"Authorization": f"Bearer {os.getenv('MCP_API_KEY')}"}
    ),
    tool_filter=["create_jira_ticket", "update_confluence_page", "create_github_issue"]
)

LlmAgent(
  name="test_generator",
  model="gemini-1.5-pro",
  instruction="Write minimal JUnit or Playwright tests for the given method or feature",
)

