import asyncio
import os
from dotenv import load_dotenv

from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.messages import TextMessage
from autogen_ext.models.openai import OpenAIChatCompletionClient

load_dotenv()


def _create_model_client(model_name: str):
    return OpenAIChatCompletionClient(
        model=model_name,
        base_url=os.getenv("OPENROUTER_BASE_URL"),
        api_key=os.getenv("OPENROUTER_API_KEY"),
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": "unknown"
        }
    )


async def _stream_agent_async(prompt: str, model_name: str):
    model_client = _create_model_client(model_name)

    assistant = AssistantAgent(
        name="assistant",
        model_client=model_client
    )

    stream = assistant.on_messages_stream(
        messages=[TextMessage(content=prompt, source="user")],
        cancellation_token=None
    )

    full_text = ""

    async for event in stream:
        if hasattr(event, "content") and event.content:
            full_text += event.content
            yield full_text

        elif hasattr(event, "chat_message"):
            if event.chat_message and event.chat_message.content:
                full_text = event.chat_message.content
                yield full_text


def stream_agent(prompt: str, model_name: str):
    async def collect():
        async for chunk in _stream_agent_async(prompt, model_name):
            yield chunk

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    agen = collect()

    try:
        while True:
            yield loop.run_until_complete(agen.__anext__())
    except StopAsyncIteration:
        pass
    finally:
        loop.close()