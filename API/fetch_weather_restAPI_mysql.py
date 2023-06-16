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

from flask import Flask, jsonify,request
from flaskext.mysql import MySQL

#assign a Flask Class
app=Flask(__name__)

#assign Flask-Mysql Module
mysql = MySQL()

#Configure MySQL
app.config['MYSQL_DATABASE_USER'] = 'diyaupradeep'
app.config['MYSQL_DATABASE_PASSWORD'] = 'diyaupradeep'
app.config['MYSQL_DATABASE_DB'] = 'iot_diya'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

#initialise MySQL (connect to mysql)
mysql.init_app(app)

#Create 1st API function for testing
#once you open "localhost:<port>/" this function is executed.
#this is not mandatory but will help in testing the program

@app.route('/')
#Give a funtion name
def welcome():
#return is the data given by the API
	return "\tWelcome.... \tKindly use one of the APIs to get data"

#Create your first real API- "recentlocation" is the API that gives recent device location
#This API will fetch data from the MySQL Database and display it on the URL

@app.route('/API1')
def recentlocation():
#Create a MySQL Cursor	
	cur = mysql.connect().cursor()
#Execute the SQL
	cur.execute('select * from <weather_data> ORDER BY id DESC LIMIT 5 ')
#Receive the SQL Response in a variable
	r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
#Return the respose to the URL
	return jsonify({'Data' : r})

#Start the Flask program
if __name__ == '__main__':
#app.run will make the APIs available on this particular IP address and Port 5000
#0.0.0.0  ip means any one can access.
    app.run(host="0.0.0.0",debug=1)
