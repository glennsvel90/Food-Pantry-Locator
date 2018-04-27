import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# Google API (requires API key)
api_key = 'AIzaSy_____________________6Hw'

# Base api url  with json output
serviceurl = "https://maps.googleapis.com/maps/api/place/textsearch/json?"


#Deal with SSL certificate anomalies Python > 2.7
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#scontext = None

conn = sqlite3.connect('geodata.sqlite')
cur = conn.cursor()

# cache the json geodata
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

fh = open("where.data")
count = 0
for line in fh:
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break
    # make address of the locations in where.data be stored as address variable
    address = line.strip()
    print('')
    # see if there is already data in the database that has the addresses that is stored in the variable 
    cur.execute("SELECT geodata FROM Locations WHERE address= ?", (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database ",address)
        continue
    except:
        pass
    # get api data from url for specific address
    print('Resolving', address)
    url = serviceurl + urllib.parse.urlencode({"key": api_key, "query": address})



    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=scontext)
    data = uh.read().decode()
    print('Retrieved',len(data),'characters',data[:20].replace('\n',' '))
    count = count + 1


    try:
        js = json.loads(str(data))
        # print js  # We print in case unicode causes an error
    except:
        continue

    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', ( memoryview(address.encode()),memoryview(data.encode()) ) )
    conn.commit()
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can visualize it on a map.")
