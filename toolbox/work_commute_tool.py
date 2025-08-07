@tool
def Get_Work_Commute(task:str, commute=max_commute) -> str:
    
    f"""
    This is the tool you will use to get the work commute (max commute = {commute}) for your user. He only cares about using Google Maps for 
    his commute calculations and he does not use the BUS or the Silver Line.
    
    Args:
        task:  the task for which to get the user's commute time
    """

    model = OpenAIServerModel(model_id="gpt-4o-mini",api_key=openai_api_key)
    
    return task