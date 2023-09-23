import requests
import json

class GetPrograms:

    def get_programs(self):
        # Define the API endpoint URL
        URL = "http://data.cityofnewyork.us/resource/uvks-tn5n.json"

        # Make an API request to retrieve data
        response = requests.get(URL)
        return response.content

    def program_school(self):
        # Initialize a list to store program agencies
        programs_list = []

        # Parse the API response into JSON format
        programs = json.loads(self.get_programs())

        # Extract and store the program agencies
        for program in programs:
            programs_list.append(program["agency"])

        return programs_list

# Create an instance of GetPrograms
programs = GetPrograms()

# Get a list of program agencies
programs_schools = programs.program_school()

# Print unique school names from the programs
for school in set(programs_schools):
    print(school)

