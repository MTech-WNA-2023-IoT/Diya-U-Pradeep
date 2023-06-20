import json
from urllib.request import urlopen
import pymysql
import mysql.connecor

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
print(data)
# Connect to MySQL database
db = mysql.connector.connect(
    host='0.0.0.0',
    user='pi',
    password='raspberry',
    database='API'
)
# Execute the create table query
db_cursor = db.cursor()
# db_cursor.execute(create_table_query)

#Import pymysql module library
import pymysql
import mysql.connecor
#Create a connection to MySQL Database 
#conn =pymysql.connect(database="iot_diya",user="diyaupradeep",password="diyaupradeep",host="localhost")
sql = """
INSERT INTO `weather_data` (`location_name`, `region`, `country`, `latitude`, `longitude`, `timezone_id`, `localtime_epoch`, `localtime`)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
# Prepare the values for the SQL statement
values = (location_data["name"],location_data["region"],location_data["country"],location_data["lat"],location_data["lon"],location_data["tz_id"],location_data["localtime_epoch"],location_data["localtime"])


# Execute the SQL statement
db_cursor.execute(sql, values)
# Commit the changes

db.commit()

# Close the connection

db.close()

# print("Raw Data")
# print(json_api)

print("Data saved to MySQL successfully!")          
          

