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

issue_creator = LlmAgent(
    name="issue_creator",
    model="gemini-2.5-pro",
    description="Creates JIRA/GitHub issues or Confluence updates for the exception fix.",
    instruction=ISSUE_CREATOR_PROMPT,
    tools=mcp_tools.tools
)
