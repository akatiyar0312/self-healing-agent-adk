from google.adk.agents import LlmAgent
from .prompt import FIX_SUGGESTER_PROMPT

fix_suggester_agent = LlmAgent(
    name="fix_suggester",
    model="gemini-2.5-pro",
    description="Suggests root cause and fix for Java/Spring Boot exceptions based on logs and code context.",
    instruction=FIX_SUGGESTER_PROMPT,
)
