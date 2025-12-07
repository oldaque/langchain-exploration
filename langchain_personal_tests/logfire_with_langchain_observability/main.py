from dotenv import load_dotenv
from env_utils import doublecheck_env
from random import randint

# Load environment variables from .env
load_dotenv()

# Check and print results
doublecheck_env(".env")  # check environmental variables


import logfire

from langchain.agents import create_agent

logfire.configure()


def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


math_agent = create_agent('google_genai:gemini-2.5-flash-lite', tools=[add], name='math_agent')

result = math_agent.invoke({'messages': [{'role': 'user', 'content': f"what's {randint(1, 100)} + {randint(1, 100)}?"}]})
print(result['messages'][-1].content)