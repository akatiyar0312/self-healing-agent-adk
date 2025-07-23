# fix_suggester.py
from google.adk.agents import LlmAgent
from .prompt import FIX_SUGGESTER_PROMPT

# Simple Agent without tools, just uses the model and a prompt
fix_suggester = LlmAgent(
    name="fix_suggester",
    model="gemini-2.5-pro",
    description="Suggests Java code fixes based on exception and context.",
    instruction=FIX_SUGGESTER_PROMPT
)
