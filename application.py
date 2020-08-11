# from flask import Flask
from flask import Flask, request, render_template,redirect
import sqltest
from time import time
import os
import redisConn
import random
import csv
import plotly
import json
import pyodbc

app = Flask(__name__)

port = int(os.getenv("PORT", 5001))
print(port)

@app.route('/Assignment4/one')
def One():
	return app.send_static_file('one.html')


@app.route('/Assignment4/three', methods = ['GET'])
def One_get():
	return app.send_static_file('three_1.html')

@app.route('/Assignment4/three', methods = ['POST'])
def Three():
	latitude1 = request.form['latitude1']
	latitude2 = request.form['latitude2']
	longitude1 = request.form['longitude1']
	longitude2 = request.form['longitude2']
	print(latitude1)
	print(latitude2)
	print(longitude1)
	print(longitude2)
	cursor = sqltest.cnxn.cursor()
	if(int(latitude1) < int(latitude2)):
		print("in lat cond")
		x1 = latitude1
		x2 = latitude2
	else:
		x1 = latitude2
		x2 = latitude1
	if(int(longitude1) < int(longitude2)):
		print("in long cond")
		y1 = longitude1
		y2 = longitude2
	else:
		y1 = longitude2
		y2 = longitude1
	print(x1)
	print(x2)
	print(y1)
	print(y2)
	print("SELECT Lat,Long from minnow where Lat between "+str(int(x1))+" and "+str(int(x2))+" and Long between "+str(int(y1))+" and "+str(int(y2)))
	cursor.execute("SELECT Lat,Long from minnow where Lat between "+str(int(x1))+" and "+str(int(x2))+" and Long between "+str(int(y1))+" and "+str(int(y2)))
	rows=cursor.fetchall()
	result = []
	print(rows)
	print("--------------------------------------------------------------------------")
	for row in rows:
		result.append([int(row[0]), int(row[1])])
	print(result)
	return render_template('three.html',rows=result)

@app.route('/Assignment4/two')
def Two():
	cursor = sqltest.cnxn.cursor()
	print('hello')
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '0' and \"Age\" < '10'")
	row1=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '10' and \"Age\" < '20'")
	row2=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '20' and \"Age\" < '30'")
	row3=cursor.fetchone()
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '30' and \"Age\" < '40'")
	row4=cursor.fetchone()
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '40' and \"Age\" < '50'")
	row5=cursor.fetchone()
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '50' and \"Age\" < '60'")
	row6=cursor.fetchone()
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '60' and \"Age\" < '70'")
	row7=cursor.fetchone()
	cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '70' and \"Age\" < '80'")
	row8=cursor.fetchone()
	print('hello')
	rows=[row1[0],row2[0],row3[0],row4[0],row5[0],row6[0],row7[0],row8[0]]
	print(row1[0])
	print(row2[0])
	print(row3[0])
	print(row4[0])
	print('hello')
	return render_template('two.html',rows=rows)

@app.route('/bar-chart')
def bar_chart_post():
	cursor = sqltest.cnxn.cursor()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '1' and \"mag\" < '2'")
	row1=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '2' and \"mag\" < '3'")
	row2=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '3' and \"mag\" < '4'")
	row3=cursor.fetchone()
	print('hello')
	rows=[row1[0],row2[0],row3[0]]
	print(row1[0])
	print(row2[0])
	print(row3[0])
	print('hello')
	return render_template('barchart.html',rows=rows)

@app.route('/bar-chart-vertical')
def bar_chart_vertical_post():
	cursor = sqltest.cnxn.cursor()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '1' and \"mag\" < '2'")
	row1=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '2' and \"mag\" < '3'")
	row2=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '3' and \"mag\" < '4'")
	row3=cursor.fetchone()
	print('hello')
	rows=[row1[0],row2[0],row3[0]]
	print(row1[0])
	print(row2[0])
	print(row3[0])
	print('hello')
	return render_template('barchart_vertical.html',rows=rows)

@app.route('/bar-chart-inverted')
def bar_chart_invert_post():
	cursor = sqltest.cnxn.cursor()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '1' and \"mag\" < '2'")
	row1=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '2' and \"mag\" < '3'")
	row2=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '3' and \"mag\" < '4'")
	row3=cursor.fetchone()
	print('hello')
	rows=[row1[0],row2[0],row3[0]]
	print(row1[0])
	print(row2[0])
	print(row3[0])
	print('hello')
	return render_template('barchart_inverted.html',rows=rows)


@app.route('/pie-chart')
def pie_chart_post():
	cursor = sqltest.cnxn.cursor()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '1' and \"mag\" < '2'")
	row1=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '2' and \"mag\" < '3'")
	row2=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '3' and \"mag\" < '4'")
	row3=cursor.fetchone()
	print('hello')
	rows=[row1[0],row2[0],row3[0]]
	print(row1[0])
	print(row2[0])
	print(row3[0])
	print('hello')
	return render_template('pie-chart.html',rows=rows)

@app.route('/scatter-plot')
def scatter_plot_post():
	cursor = sqltest.cnxn.cursor()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '1' and \"mag\" < '2'")
	row1=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '2' and \"mag\" < '3'")
	row2=cursor.fetchone()
	print('hello')
	cursor.execute("SELECT count(mag) from quake6 where \"mag\" > '3' and \"mag\" < '4'")
	row3=cursor.fetchone()
	print('hello')
	rows=[row1[0],row2[0],row3[0]]
	print(row1[0])
	print(row2[0])
	print(row3[0])
	print('hello')
	return render_template('scatter-plot.html',rows=rows)

@app.route('/without-cache', methods=['GET'])
def without_cache_get():
    return app.send_static_file('my-form.html')

@app.route('/without-cache', methods=['POST'])
def without_cache_post():
	number = request.form['Number']
	mag = request.form['mag']
	countTime = 0
	while(int(number) > 0 and int(number) < 1001):
		cursor = sqltest.cnxn.cursor()
		tic = time()
		cursor.execute("SELECT COUNT(*) from all_month WHERE mag >'" + mag + "'")
		row = cursor.fetchone()
		toc = time()
		countTime = countTime + toc - tic
		tic1 = 0
		toc1 = 0
		while row:
			tic1 = time()
			row = cursor.fetchone()
			toc1 = time()
			countTime = countTime + toc1 - tic1
		number = int(number) - 1
		print(number)
	return "Time count: " + str(float(countTime))


@app.route('/quiz1', methods=['GET'])
def quiz1get():
    return app.send_static_file('quiz31.html')

@app.route('/quiz1', methods=['POST'])
def quiz1_post():
	Point1 = request.form['depth1']
	Point2 = request.form['depth2']
	l1 = request.form['longitude']
	#mag = str(random.uniform(1.5,1.9))
	#countTime = 0
	#while(int(number) > 0 and int(number) < 1001):
	cursor = sqltest.cnxn.cursor()
	#tic = time()
	row=[]
	cursor.execute("SELECT * from quake6 where \"depthError\">" + Point1 + " and \"depthError\"< " + Point2 + " and \"longitude\" ='" + l1 +"'")
	rows = cursor.fetchone()
	while rows != False:
		x = {}
		x['time'] = str(rows["time"]) 
		x['latitide'] = str(rows["latitude"])
		x['longitude'] = str(rows["longitude"])
		x['depthError'] = str(rows["depthError"]) 
		row.append(x)
		rows=cursor.fetchone()

	html = """<!DOCTYPE html>
	<html>
	<head>
	<title> Hello </title>
	</head>
	<body>
	<h1>SWETA NITINBHAI GADHIYA_1001720114</h1>
	<p>"""
	for i in row: 
		for attr, value in i.items():
			if(attr == 'time'):
				html = html + value + "<br>"
			if(attr == 'latitude'):
				html = html + value + "<br>"
			if(attr == 'longitude'):
				html = html + str(value) + "<br>"
			if(attr == 'depthError'):
				html = html + str(value) + "<br>"

	html = html + "</p>"
	html = html + "</html>"
	print(html)
	return html

@app.route('/without-cache-select', methods=['GET'])
def without_cache_select_get():
    return app.send_static_file('my-form2.html')

@app.route('/without-cache-select', methods=['POST'])
def without_cache_select_post():
	number = request.form['Number']
	mag = str(random.uniform(1.5,1.9))
	countTime = 0
	while(int(number) > 0 and int(number) < 1001):
		cursor = sqltest.cnxn.cursor()
		tic = time()
		cursor.execute("SELECT * from all_month WHERE mag >'" + mag + "'")
		row = cursor.fetchone()
		toc = time()
		countTime = countTime + toc - tic
		tic1 = 0
		toc1 = 0
		while row:
			tic1 = time()
			row = cursor.fetchone()
			toc1 = time()
			countTime = countTime + toc1 - tic1
		number = int(number) - 1
		print(number)
	return "Time count: " + str(float(countTime))
@app.route('/with-cache')
def my_form():
    return app.send_static_file('my-form.html')

@app.route('/with-cache', methods=['POST'])
def my_form_post():
	number = request.form['Number']
	mag = request.form['mag']
	print()
	countTime = 0
	while(int(number) > 0 and int(number) < 1001):
		tic = time()
		isExist = redisConn.r.get(str(mag))
		toc = time()
		countTime = countTime + toc - tic
		if(isExist):
			number = int(number) - 1
			continue
		print(countTime)
		cursor = sqltest.cnxn.cursor()
		tic1 = time()
		cursor.execute("SELECT COUNT(*) from quake6 WHERE mag >'" + mag + "'")
		row = cursor.fetchone()
		toc1 = time()
		r2Tic = 0
		r2Toc = 0
		while row:
			r2Tic = time()
			redisConn.r.set(str(mag), str(row[0]))
			row = cursor.fetchone()
			r2Toc = time()
		number = int(number) - 1
		countTime = countTime + toc1 - tic1 + r2Toc - r2Tic
		print(number)
	return "Time count: " + str(float(countTime)) 

@app.route('/with-cache-select')
def my_form_cache_select_get():
    return app.send_static_file('my-form3.html')

@app.route('/with-cache-select', methods=['POST'])
def my_form_cache_select_post():
	number = request.form['Number']
	mag1 = request.form['mag1']
	mag2 = request.form['mag2']
	print()
	countTime = 0
	while(int(number) > 0 and int(number) < 1001):
		tic = time()
		isExist = redisConn.r.get(str(mag))
		toc = time()
		countTime = countTime + toc - tic
		if(isExist):
			number = int(number) - 1
			continue
		print(countTime)
		cursor = sqltest.cnxn.cursor()
		tic1 = time()
		cursor.execute("SELECT * from all_month WHERE mag >'" + mag1 + "'")
		row = cursor.fetchone()
		toc1 = time()
		r2Tic = 0
		r2Toc = 0
		while row:
			r2Tic = time()
			redisConn.r.set(str(mag), str(row[4]))
			row = cursor.fetchone()
			r2Toc = time()
		number = int(number) - 1
		countTime = countTime + toc1 - tic1 + r2Toc - r2Tic
		print(number)
	return "Time count: " + str(float(countTime)) 


@app.route('/with-cache-question')
def my_form_question_get():
    return app.send_static_file('my-form3.html')

@app.route('/with-cache-question', methods=['POST'])
def my_form_question_post():
	print("hello")
	number = request.form['Number']
	depth1 = request.form['depth1']
	depth2 = request.form['depth2']
	print("hello2")
	countTime = 0
	firstTime = 0
	small = 0
	large = 0
	loactionForFirstSelect = set()
	print("hello3")
	while(int(number) > 0 and int(number) < 1001):
		loactionForFirstSelectCache = set()
		magRand1 = random.randint(float(depth1)*10, float(depth2)*10)
		magRand2 = random.randint(float(depth1)*10, float(depth2)*10)
		print(magRand1)
		print(magRand2)
		print(float(magRand1) / 10)
		print(float(magRand2) / 10)
		small = (float(magRand1) / 10.0)
		large = (float(magRand2) / 10.0)
		if(magRand1 > magRand2):
			tmp = small
			small = large
			large = tmp
		print(small)
		print(large)
		tic = time()
		isExist = redisConn.r.get(str(small)+'-'+str(large))
		toc = time()
		countTime = countTime + toc - tic
		if(isExist):
			if(int(number) == int(request.form['Number'])):
				firstTime = countTime
				loactionForFirstSelect = isExist
			number = int(number) - 1
			print('Cache Hit.')
			continue
		print('Cache Miss.')
		print(countTime)
		cursor = sqltest.cnxn.cursor()
		tic1 = time()
		cursor.execute("SELECT * from quake6 WHERE depthError >'" + str(small) + "' and depthError <'" + str(large) + "'")
		rows = cursor.fetchall()
		toc1 = time()
		for row in rows:
			if(int(number) == int(request.form['Number'])):
				loactionForFirstSelect.add('<br>' + str(row[1]))	
			#x = {}
			#x["time"] = str(row[0])
			#x["mag"] = str(row[4])
			loactionForFirstSelectCache.add('<br>' + str(row[1]))			
		r2Tic = time()
		#for multiple columns:
		#redisConn.r.set(str(small) + '-' + str(large), x)
		#Above, x is json object and "str(small) + '-' + str(large)" is key which will be dynamic and will look like 3.5-4.2 in this case.
		#but if question has input parameters are mag and location then our dynamic key will be 3.5-au where 3.5 is mag and au is location.
		redisConn.r.set(str(small) + '-' + str(large), str(loactionForFirstSelectCache))
		r2Toc = time()
		countTime = countTime + toc1 - tic1 + r2Toc - r2Tic
		if(int(number) == int(request.form['Number'])):
				firstTime = countTime
		number = int(number) - 1
		print(number)
	return "Total Time Count: " + str(float(countTime)) + "<br> First Location: " + str(loactionForFirstSelect) + "<br> First Result Time: " + str(float(firstTime))

@app.route('/create-table-index')
def create_table_index():
	cursor = sqltest.cnxn.cursor()
	tic = time()
	cursor.execute("CREATE TABLE Person2( PersonId INT IDENTITY PRIMARY KEY, FirstName NVARCHAR(128) NOT NULL, MiddelInitial NVARCHAR(10), LastName NVARCHAR(128) NOT NULL, DateOfBirth DATE NOT NULL)")
	#cursor.execute("CREATE TABLE Student1( StudentId INT IDENTITY PRIMARY KEY, PersonId INT REFERENCES Person1 (PersonId), Email NVARCHAR(256) )")
	toc = time()
	cursor.close()
	sqltest.cnxn.commit()
	return str(float(toc-tic))

@app.route('/')
def hello_world():
  return 'Hello, World!\n This looks just amazing within 5 minutes'



if __name__ == '__main__':
	app.run(host='0.0.0.0', port=port)

