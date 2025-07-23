import json
from concurrent.futures import TimeoutError
from google.cloud import pubsub_v1
from google.adk.agents import LlmAgent  # Your LLM setup

# Pub/Sub settings
PROJECT_ID = "your-gcp-project-id"
SUBSCRIPTION_ID = "your-subscription-id"
TIMEOUT = 60.0  # seconds

# Create log analyzer agent (use your own logic or import)
log_analyzer = LlmAgent(
    name="log_analyzer",
    model="gemini-1.5-pro",
    instruction="""
You are a log analysis agent. Analyze the log and classify:
- severity (ERROR, WARN, INFO)
- error type
- resolution (UI_FIXABLE, BUG_REPORT, UNKNOWN)
Respond in JSON.
"""
)

# Callback to process each message
def callback(message: pubsub_v1.subscriber.message.Message) -> None:
    try:
        payload = json.loads(message.data.decode("utf-8"))
        log_entry = payload.get("protoPayload") or payload.get("jsonPayload") or payload

        # Analyze using your agent
        result = log_analyzer.analyze(log_entry)
        print(f"Log: {log_entry.get('message', '')}")
        print(f"Analysis: {json.dumps(result, indent=2)}")

        message.ack()
    except Exception as e:
        print(f"Failed to process message: {e}")
        message.nack()

def main():
    subscriber = pubsub_v1.SubscriberClient()
    subscription_path = subscriber.subscription_path(PROJECT_ID, SUBSCRIPTION_ID)

    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    print(f"Listening for messages on {subscription_path}...")

    try:
        streaming_pull_future.result(timeout=TIMEOUT)
    except TimeoutError:
        streaming_pull_future.cancel()

