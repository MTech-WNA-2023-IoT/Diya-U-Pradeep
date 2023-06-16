import json
from urllib.request import urlopen
#Create user account and obtain API key from https://www.weatherapi.com

url = "https://api.weatherapi.com/v1/current.json?key=4e06a340688349e18e3151111231506&q=kollam&aqi=no"

api_page = urlopen(url)
api=api_page.read()
json_api=json.loads(api)
#data1= json_api['current']
#print(data1)
print("Raw Data")
print(json_api)

print("Parsed")
data= json_api['location']
#print(data)
