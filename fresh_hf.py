import os
import sys
from dotenv import load_dotenv
from smolagents import ApiWebSearchTool, CodeAgent, InferenceClientModel, DuckDuckGoSearchTool, WikipediaSearchTool

# Load environment variables from .env file
load_dotenv()

# Get API key from environment
hf_api_key = os.getenv("HF_API_KEY")
if not hf_api_key:
    raise ValueError("ur silly")

model = InferenceClientModel(api_key=hf_api_key)
agent = CodeAgent(
    tools=[DuckDuckGoSearchTool()],
    model=model,
)

approved_sources = ["zillow", "apartments.com", "homes.com rent"]
neighboorhoods = ["allston", "brighton", "brookline", "quincy"]
rent = "$2400"
work_address = "545 Commonwealth Ave., Boston, MA"
max_commute = "30 minutes"
banned_transport = ["Bus","Silver Line","Uber","Lyft"]

try:
    agent.run(f"Look for 20 apartments in {', '.join(neighboorhoods)} for {rent} or less")
except KeyboardInterrupt:
    print("user interrupt")
    

#Filter Apartments
def filterApartments(work=work_address, commute=max_commute, wont_take=banned_transport):
    pass  # TODO: Implement filtering logic

