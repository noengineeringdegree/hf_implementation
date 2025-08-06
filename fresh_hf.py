import os
import sys
from litellm import completion
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel, DuckDuckGoSearchTool


approved_sources = ["zillow", "apartments.com", "homes.com rent"]
neighboorhoods = ["allston", "brighton", "brookline", "quincy"]
rent = "$2400"
work_address = "545 Commonwealth Ave., Boston, MA"
max_commute = "30 minutes"
banned_transport = ["Bus","Silver Line","Uber","Lyft"]

# Load environment variables from .env file
load_dotenv()
hf_api_key = os.getenv("OPENAI_KEY")
if not hf_api_key:
    raise ValueError("ur silly")
model = OpenAIServerModel(model_id="gpt-4o-mini",api_key="OPENAI_KEY")
agent = CodeAgent(tools=[],model="gpt-4o-mini")
CodeAgent()

try:
    agent.run(f"Look for 20 apartments in {', '.join(neighboorhoods)} for {rent} or less")
except KeyboardInterrupt:
    print("user interrupt")
    

#Filter Apartments
def filterApartments(work=work_address, commute=max_commute, wont_take=banned_transport):
    pass  # TODO: Implement filtering logic
