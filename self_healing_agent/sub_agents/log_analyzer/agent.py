from google.adk.agents import LlmAgent

log_analyzer = LlmAgent(
    name="log_analyzer",
    model="gemini-1.5-pro",
    instruction="Analyze the logs for error patterns.",
)
