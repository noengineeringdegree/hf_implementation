import os
import sys
from litellm import completion
from dotenv import load_dotenv
from smolagents import CodeAgent, OpenAIServerModel, Tool


approved_sources = ["zillow", "apartments.com", "homes.com rent"]
neighboorhoods = ["allston", "brighton", "brookline", "quincy"]
rent = "$2400"
work_address = "545 Commonwealth Ave., Boston, MA"
max_commute = "30 minutes"
banned_transport = ["Bus","Silver Line","Uber","Lyft"]


class Get_Work_Commute(Tool):
    name = "get_work_time"
    description = """
    This is the tool you will use to get the work commute for your user. He only cares about using Google Maps for 
    his commute calculations and he does not use the BUS or the Silver Line.
    """
    inputs = {
        "task": {
            "type": "string",
            "description": "origin-destination travel time by subway only",
        }
    }
    output_type = "string"

    def forward(self, task: str):
        from smolagents import OpenAIServerModel

        model = OpenAIServerModel(model_id="gpt-4o-mini",api_key=openai_api_key)
        return model.id

get_work_time = Get_Work_Commute()


# Load environment variables from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_KEY")
if not openai_api_key:
    raise ValueError("ur silly")
model = OpenAIServerModel(model_id="gpt-4o-mini",api_key=openai_api_key)
agent = CodeAgent(tools=[get_work_time],model=model)

try:
    agent.run(f"Look for 20 apartments in {', '.join(neighboorhoods)} for {rent} or less")
except KeyboardInterrupt:
    print("user interrupt")


#Filter Apartments
def filterApartments(work=work_address, commute=max_commute, wont_take=banned_transport):
    pass  # TODO: Implement filtering logic

# Use that decorator they have. Make as a seperate tools subpackage and struggle through the python import system like we all had to





