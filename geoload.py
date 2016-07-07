import urllib
import sqlite3
import json
import time
import ssl

serviceurl = "http://maps.googleapis.com/maps/api/geocode/json?"
scontext=None
conn=sqlite3.connect('geodata.sqlitle')
cur=conn.cursor()

cur.execute(''' CREATE TABLE IF NOT EXISTS locations (address TEXT, geodata TEXT)''')

fh=open("where.data")
count=0
for line in fh:
	if count > 200:
		break
	address=line.strip()
	print ""
	cur.execute("SELECT geodata FROM locations WHERE address=?", (buffer(address), ))
	#try to fetch the geodata from database
	try:
		data=cur.fetchone()[0]
		print "found in database ",address
		continue
	except:
		pass
	print "Resolving" , address
	url=serviceurl+urllib.urlencode({"sensor":"false", "address": address})
	print "Retrieving", url
	uh=urllib.urlopen()









































