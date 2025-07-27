import json
import requests
from flask import Flask

# API endpoint URL's and access keys
WMATA_API_KEY = "5943f016ed1d428aa93b69836b1fc529"
INCIDENTS_URL = "https://api.wmata.com/Incidents.svc/json/ElevatorIncidents"
headers = {"api_key": WMATA_API_KEY, 'Accept': '*/*'}

################################################################################

app = Flask(__name__)

# get incidents by machine type (elevators/escalators)
# field is called "unit_type" in WMATA API response
@app.route("/incidents/<unit_type>", methods=["GET"])
def get_incidents(unit_type):
  # create an empty list called 'incidents'
  incidents = []

  # use 'requests' to do a GET request to the WMATA Incidents API
  response = requests.get(INCIDENTS_URL, headers=headers)
  # retrieve the JSON from the response
  data = response.json()
  # iterate through the JSON response and retrieve all incidents matching 'unit_type'
  # for each incident, create a dictionary containing the 4 fields from the Module 7 API definition
  #   -StationCode, StationName, UnitType, UnitName
  # add each incident dictionary object to the 'incidents' list
  for item in data.get('ElevatorIncidents', []):
        if unit_type == "elevators" and item.get("UnitType") == "ELEVATOR":
            incidents.append({
                "StationCode": item.get("StationCode"),
                "StationName": item.get("StationName"),
                "UnitName": item.get("UnitName"),
                "UnitType": item.get("UnitType"),
            })

        if unit_type == "escalators" and item.get("UnitType") == "ESCALATOR":
            incidents.append({
                "StationCode": item.get("StationCode"),
                "StationName": item.get("StationName"),
                "UnitName": item.get("UnitName"),
                "UnitType": item.get("UnitType"),
            })
  # return the list of incident dictionaries using json.dumps()
  return json.dumps(incidents)
if __name__ == '__main__':
    app.run(debug=True)
