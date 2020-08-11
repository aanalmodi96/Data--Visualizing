
from flask import Flask, render_template, request
import sqlite3 as sql
from datetime import datetime
from json import loads, dumps
# import pandas as pd
import random
import time
import redis
import hashlib
# from werkzeug.utils import secure_filename


app = Flask(__name__)


#myHostname = "aanal1.redis.cache.windows.net"
#myPassword = "EtnrCtH+NwcKrxJMw9tcCFcz3L5Jun+KyLNaD0lH7xA="
#r = redis.StrictRedis(host=myHostname, port=6380,password=myPassword,ssl=True)


#import pyodbc
#server = 'priyal.database.windows.net'
#database = 'AssignmentQuiz4'
#username = 'aanalpriyal'
#password = '1!Sspnnham'
#driver= '{ODBC Driver 13 for SQL Server}'
#cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()

@app.route('/')
def main():
    cnxn = sql.connect("db.db")
    cursor = cnxn.cursor()
    cursor.execute("SELECT * from titanic3")
    rows=cursor.fetchall()

    cursor.close()
    cnxn.close()
    print(rows)
    print('Jees')

    return str(rows)
    #return render_template('main.html', rows=rows)



# @app.route('/barchart', methods=['GET','POST'])
# def barchart():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#     print(cnxn)
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('barchart.html', rows=rows)
#
# @app.route('/faltu', methods=['GET','POST'])
# def faltu():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#     print(cnxn)
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('faltu.html', rows=rows)
#
#
# @app.route('/bartrial', methods=['GET','POST'])
# def bartrial():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' +
#                           database
#                           + ';UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '0' and \"Age\" < '10'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '10' and \"Age\" < '20'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '20' and \"Age\" < '30'")
#     row3 = cursor.fetchone()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '30' and \"Age\" < '40'")
#     row4 = cursor.fetchone()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '40' and \"Age\" < '50'")
#     row5 = cursor.fetchone()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '50' and \"Age\" < '60'")
#     row6 = cursor.fetchone()
#     cursor.execute("SELECT count(Age) from Minnow where \"Age\" >= '60' and \"Age\" < '70'")
#     row7 = cursor.fetchone()
#     print("neha")
#     cursor.execute("SELECT count(Age) from minnow where \"Age\" >= '70' and \"Age\" < '80'")
#     row8 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0], row4[0], row5[0], row6[0], row7[0], row8[0]]
#     print(rows)
#
#     return render_template('bartrial.html', rows=rows)
#
#
# @app.route('/updown', methods=['GET','POST'])
# def updown():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('updown.html', rows=rows)
#
# @app.route('/piechart', methods=['GET','POST'])
# def piechart():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT count(mag) from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('piechart.html', rows=rows)
#
# @app.route('/scatter', methods=['GET','POST'])
# def scatter():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('scatter.html', rows=rows)
#
#
# @app.route('/three', methods = ['GET'])
# def three():
# 	return render_template('three_1.html')
#
# @app.route('/three', methods = ['POST'])
# def Three():
#
# 	latitude1 = request.form['latitude1']
# 	latitude2 = request.form['latitude2']
# 	longitude1 = request.form['longitude1']
# 	longitude2 = request.form['longitude2']
# 	print(latitude1)
# 	print(latitude2)
# 	print(longitude1)
# 	print(longitude2)
# 	cursor = cnxn.cursor()
# 	if(int(latitude1) < int(latitude2)):
# 		print("in lat cond")
# 		x1 = latitude1
# 		x2 = latitude2
# 	else:
# 		x1 = latitude2
# 		x2 = latitude1
# 	if(int(longitude1) < int(longitude2)):
# 		print("in long cond")
# 		y1 = longitude1
# 		y2 = longitude2
# 	else:
# 		y1 = longitude2
# 		y2 = longitude1
# 	print(x1)
# 	print(x2)
# 	print(y1)
# 	print(y2)
# 	print("SELECT Lat,Long from minnow where Lat between "+str(int(x1))+" and "+str(int(x2))+" and Long between "+str(int(y1))+" and "+str(int(y2)))
# 	cursor.execute("SELECT Lat,Long from minnow where Lat between "+str(int(x1))+" and "+str(int(x2))+" and Long between "+str(int(y1))+" and "+str(int(y2)))
# 	rows=cursor.fetchall()
# 	result = []
# 	print(rows)
# 	print("--------------------------------------------------------------------------")
# 	for row in rows:
# 		result.append([int(row[0]), int(row[1])])
# 	print(result)
# 	return render_template('three.html',rows=result)
#
#
# @app.route('/barchart_vertical', methods=['GET','POST'])
# def barchart_vertical():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('barchart_vertical.html', rows=rows)
#
#
# @app.route('/barchart_inverted', methods=['GET','POST'])
# def barchart_inverted():
#     cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1443;DATABASE=' + database
#                           + ';UID=' + username + ';PWD=' + password)
#
#     cursor = cnxn.cursor()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '1' and \"mag\" < '2'")
#     row1 = cursor.fetchone()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '2' and \"mag\" < '3'")
#     row2 = cursor.fetchone()
#     cursor.execute("SELECT depth from dbo.all_month where \"mag\" > '3' and \"mag\" < '4'")
#     row3 = cursor.fetchone()
#
#     rows = [row1[0], row2[0], row3[0]]
#     return render_template('barchart_inverted.html', rows=rows)
#
#
# '''@app.route('/createtable')
# def createTable():
#     lstDictionaryData = []
#     conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = conn.cursor()
#     # query = "CREATE TABLE dbo.all_month (\"time\" datetime, \"latitude\" FLOAT, \"longitude\" FLOAT, \"depth\" FLOAT, \"mag\" FLOAT, \"magType\" TEXT, \"nst\" INT, \"gap\" INT, \"dmin\" FLOAT, \"rms\" FLOAT, \"net\" TEXT, \"id\" TEXT, \"updated\" datetime, \"place\" TEXT, \"type\" TEXT, \"horontalError\" FLOAT, \"depthError\" FLOAT, \"magError\" FLOAT, \"magNst\" INT, \"status\" TEXT, \"locationSource\" TEXT, \"magSource\" TEXT)"
#     query = "CREATE TABLE dbo.all_month(time DATETIME,latitude FLOAT,longitude FLOAT,depth FLOAT,mag FLOAT,magType TEXT,nst INT,gap INT,dmin FLOAT,rms FLOAT,net TEXT,id TEXT,updated DATETIME,place TEXT,type TEXT,horontalError FLOAT,depthError FLOAT,magError FLOAT,magNst INT,status TEXT,locationSource TEXT,magSource TEXT)"
#     # print(query)
#     startTime = time.time()
#     # cursor.execute(query)
#     cursor.execdirect(query)
#     #cursor.execdirect("CREATE INDEX all_month_mag__index ON dbo.earthquake_new (mag)")
#     #cursor.execdirect("CREATE INDEX all_month_lat__index ON dbo.earthquake_new (latitude)")
#     #cursor.execdirect("CREATE INDEX all_month_long__index ON dbo.earthquake_new (longitude)")
#     endTime = time.time()
#     conn.close()
#     executionTime = (endTime - startTime) * 1000
#     return render_template('main.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__(), executionTime=executionTime)'''
#
# '''@app.route('/randomqueries')
# def randomQueries():
#     noOfQueries = int(request.args.get('queries', ''))
#     withCache = int(request.args.get('withCache', ''))
#     magnitudeStart = float(request.args.get('magnitudeStart', ''))
#     magnitudeEnd = float(request.args.get('magnitudeEnd', ''))
#
#     lstDictionaryData = []
#     lstDictionaryDataDisplay = []
#
#     conn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
#     cursor = conn.cursor()
#     totalExecutionTime = 0
#     columns = ['time', 'latitude', 'longitude', 'place', 'mag']
#
#     # without cache
#     if withCache == 0:
#         # print("hi!")
#
#         magnitude_value = round(random.uniform(magnitudeStart, magnitudeEnd), 1)
#         startTime = time.time()
#         query = "SELECT locationSource FROM dbo.all_month WHERE mag = '" + str(magnitude_value) + "'"
#         cursor.execute(query)
#         endTime = time.time()
#         # print(query)
#         lstDictionaryDataDisplay = cursor.fetchall()
#         # print(lstDictionaryDataDisplay)
#         executionTime = (endTime - startTime) * 1000
#         firstExecutionTime = executionTime
#
#         for i in range(noOfQueries-1):
#             totalExecutionTime = totalExecutionTime + executionTime
#             magnitude_value = round(random.uniform(magnitudeStart, magnitudeEnd), 1)
#             startTime = time.time()
#             query = "SELECT locationSource FROM dbo.all_month WHERE mag = '" + str(magnitude_value) + "'"
#             cursor.execute(query)
#             endTime = time.time()
#             lstDictionaryData = list(cursor.fetchall())
#             # print("inside if")
#             # print(lstDictionaryData)
#
#             memData = []
#             for row in lstDictionaryData:
#                 memDataDict = dict()
#                 for i, val in enumerate(row):
#                     if type(val) == datetime:
#                         val = time.mktime(val.timetuple())
#                     memDataDict[columns[i]] = val
#                 memData.append(memDataDict)
#             r.set(query, dumps(memData))
#
#             executionTime = (endTime - startTime) * 1000
#             # totalExecutionTime = totalExecutionTime + executionTime
#         # print(totalExecutionTime)
#     # with cache
#     else:
#         for i in range(noOfQueries):
#             magnitude_value = round(random.uniform(1, 10), 2)
#             query = "SELECT locationSource FROM dbo.all_month WHERE mag = '" + str(magnitude_value) + "'"
#             # print("inside else")
#             memhash = hashlib.sha256(query.encode()).hexdigest()
#             startTime = time.time()
#             lstDictionaryData = r.get(memhash)
#
#             # print(lstDictionaryData[0])
#             # print(i)
#             if not lstDictionaryData:
#                 # print("from db")
#
#                 cursor.execute(query)
#                 lstDictionaryData = cursor.fetchall()
#                 if i == 0:
#                     # print("from db")
#                     lstDictionaryDataDisplay = lstDictionaryData
#                 endTime = time.time()
#                 memData = []
#                 for row in lstDictionaryData:
#                     memDataDict = dict()
#                     for i, val in enumerate(row):
#                         if type(val) == datetime:
#                             val = time.mktime(val.timetuple())
#                         memDataDict[columns[i]] = val
#                     memData.append(memDataDict)
#                 r.set(memhash, dumps(memData))
#             else:
#                 lstDictionaryData = loads(lstDictionaryData.decode())
#                 if i == 0:
#                     lstDictionaryDataDisplay = lstDictionaryData
#                 endTime = time.time()
#             executionTime = (endTime - startTime) * 1000
#             if i == 0:
#                 firstExecutionTime = executionTime
#             totalExecutionTime = totalExecutionTime + executionTime
#     conn.close()
#     # print(lstDictionaryData)
#     return render_template('main.html', tableData=lstDictionaryDataDisplay, tableDataLen=lstDictionaryDataDisplay.__len__(), executionTime=totalExecutionTime, firstExecutionTime=firstExecutionTime)
# '''

# @app.route('/upload_  data', methods=['POST'])
# def upload():
#     sqlquery = 'Insert into "all_month" ({columns}) values ({values})'
#     tempfile = request.files['files']
#     filename = 'tempcsv'
#     tempfile.save(os.path.join(filename))
#
#     csv_file = open(filename, 'r')
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         cols = '"' + '","'.join(row.keys()) + '"'
#         vals = '\'' + '\',\''.join(row.values()) + '\''
#         q = sqlquery.format(columns=cols, values=vals)
#         print("QUERy:", q)
#         cursor = database.connection.cursor()
#         cursor.execute(q)
#     csv_file.close()

# @app.route('/uploaddata')
# def uploadData():
#     return render_template('index.html', tableData=lstDictionaryData, tableDataLen=lstDictionaryData.__len__())

if __name__ == '__main__':
    app.run(debug=False)