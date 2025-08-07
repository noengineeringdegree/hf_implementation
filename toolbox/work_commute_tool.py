from smolagents import tool
from smolagents import OpenAIServerModel, CodeAgent

@tool
def Get_Work_Commute(task:str) -> str:
    
    """
    This is the tool you will use to get the work commute (max commute) for your user. He only cares about using Google Maps for 
    his commute calculations and he does not use the BUS or the Silver Line.
    
    Args:
        task:  the task for which to get the user's commute time so this will only return the commute between the apartmn
    """

    model = OpenAIServerModel(model_id="gpt-4o-mini",api_key=openai_api_key)

    return task