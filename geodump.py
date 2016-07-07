import sqlite3
import json
import codecs

conn=sqlite3.connect('deodata.sqlite')
cur=conn.cursor()

cur.execute('SELECT * FROM Locations')
fhand=codecs.open('where.js','w','utf-8')
fhand.write("myData=[\n")
count=0
for row in cursor:
	data=str(row[1])
	try: 
		js=json.loads(str(data))
	except:
		continue

	if not('status' in js and js['status'] =='OK'):
		continue
	lat=js["results"][0]["geometry"]["location"]["lat"]
	lng=js["results"]