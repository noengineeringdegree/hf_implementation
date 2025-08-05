import smolagents
import datetime

class Work_Commute_Calc(Tool):
    name = "work commute calculator"
    description = """
    This is a tool that takes the user's Work Address and a potential Apartment Address and
    finds the commute in minutes in both directions.
    """
    output_type = "string"

    def forward(self, task: str)
        from 








work_location = input("Select Work Location: ")
max_commute = input("In minutes, what's the max commute time you can withstand: ")



@tool
def get_commute_time_api(address: work_location, apt_location: apt_location)
    """
    Returns the commute time to/from (bidirectionally) of the user's work address and
    listing that you found. Should be sent in minutes"

    Args:
        work_location is the address of the user's workplace
        apt_location is the apartment of interest's address 
    """

    try:
