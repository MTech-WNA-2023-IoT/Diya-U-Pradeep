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
print(data)

#Import pymysql module library
import pymysql
#Create a connection to MySQL Database 
conn =pymysql.connect(database="iot_diya",user="diyaupradeep",password="diyaupradeep",host="localhost")
#Create a MySQL Cursor to that executes the SQLs
cur=conn.cursor()
#Create a dictonary containing the fields, name, age and place
#data={'topic':'temp','data':30}
#Execute the SQL to write data to the database
cur.execute("INSERT INTO `iot_data`(`topic`,`data`)VALUES(%(topic)s,%(data)s);",data)
#Close the cursor
#cur.close()
#Commit the data to the database
conn.commit()
#Close the connection to the database
conn.close()

