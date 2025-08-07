import os
import sys
from litellm import completion
from smolagents import CodeAgent, OpenAIServerModel
from dotenv import load_dotenv

from toolbox.work_commute_tool import Get_Work_Commute

approved_sources = ["zillow", "apartments.com", "homes.com rent"]
neighboorhoods = ["allston", "brighton", "brookline", "quincy"]
rent = "$2400"
work_address = "545 Commonwealth Ave., Boston, MA"
max_commute = "30 minutes"
banned_transport = ["Bus","Silver Line","Uber","Lyft"]

# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_KEY")
if not openai_api_key:
    raise ValueError("ur silly")

model = OpenAIServerModel(model_id="gpt-4o-mini",api_key=openai_api_key)
agent = CodeAgent(tools=[Get_Work_Commute],model=model)

try:
    agent.run(f"Find the commute times for 20 apartments where work commute is equal to {work_address} and the apartments are strictly in {', '.join(neighboorhoods)} going for {rent} or less")
except KeyboardInterrupt:
    print("user interrupt")




