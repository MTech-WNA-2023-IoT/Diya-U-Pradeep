import json
from urllib.request import urlopen
import pymysql
#import mysql.connecor

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
#db = mysql.connector.connect(
 #   host='0.0.0.0',
  #  user='pi',
   # password='raspberry',
    #database='API'
#)
# Execute the create table query
# db_cursor = db.cursor()
# db_cursor.execute(create_table_query)

#Import pymysql module library
import pymysql
#import mysql.connector
#Create a connection to MySQL Database 
conn =pymysql.connect(database="iot_diya",user="diyaupradeep",password="diyaupradeep",host="localhost")
sql = """
INSERT INTO `weather_data` (`name`, `region`, `country`, `latitude`, `longitude`, `timezone_id`, `localtime_epoch`, `localtime`)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""
# Prepare the values for the SQL statement
cur=conn.cursor()
#values = (location["name"],location["region"],location["country"],location["lat"],location["lon"],location["tz_id"],location["localtime_epoch"],location["localtime"])

values = (data["name"],data["region"],data["country"],data["lat"],data["lon"],data["tz_id"],data["localtime_epoch"],data["localtime"])


# Execute the SQL statement
cur.execute(sql, values)
#db_cursor.execute(sql, values)
# Commit the changes

#db.commit()
conn.commit()
# Close the connection
conn.close()

#db.close()

# print("Raw Data")
# print(json_api)

print("Data saved to MySQL successfully!")          
          
