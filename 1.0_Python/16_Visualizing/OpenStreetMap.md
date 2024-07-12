---
id: OpenStreetMap
aliases: []
tags: []
---

# OpenStreetMap

#viz

- In this project, we are using OpenStreetMap geocoding API to clean up some user-entered geographic locations of university names and then placing the data on an actual OpenStreetMap.

```python
import urllib.request, urllib.parse, urllib.error
import http
import sqlite3
import json
import time
import ssl
import sys

# https://py4e-data.dr-chuck.net/opengeo?q=Ann+Arbor%2C+MI
serviceurl = 'https://py4e-data.dr-chuck.net/opengeo?'

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

conn = sqlite3.connect('opengeo.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

fh = open("where.data")
count = 0
nofound = 0
for line in fh:
    if count > 100 :
        print('Retrieved 100 locations, restart to retrieve more')
        break

    address = line.strip()
    print('')
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        (memoryview(address.encode()), ))

    try:
        data = cur.fetchone()[0]
        print("Found in database", address)
        continue
    except:
        pass

    parms = dict()
    parms['q'] = address

    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    count = count + 1

    try:
        js = json.loads(data)
    except:
        print(data)  # We print in case unicode causes an error
        continue

    if not js or 'features' not in js:
        print('==== Download error ===')
        print(data)
        break

    if len(js['features']) == 0:
        print('==== Object not found ====')
        nofound = nofound + 1

    cur.execute('''INSERT INTO Locations (address, geodata)
        VALUES ( ?, ? )''',
        (memoryview(address.encode()), memoryview(data.encode()) ) )

    conn.commit()

    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

if nofound > 0:
    print('Number of features for which the location could not be found:', nofound)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
```

- This program will read the input lines in _where.data_ and for each line check to see if it is already in the database.
- If we don't have the data for the location, it will call the geocoding API to retrieve the data and store it in the database.

Here's a sample run after there's already some data in the db:

```python
Found in database AGH University of Science and Technology
Found in database Academy of Fine Arts Warsaw Poland
Found in database American University in Cairo
Found in database Arizona State University
Found in database Athens Information Technology
Retrieving https://py4e-data.dr-chuck.net/
opengeo?q=BITS+Pilani
Retrieved 794 characters {"type":"FeatureColl
Retrieving https://py4e-data.dr-chuck.net/
opengeo?q=Babcock+University
Retrieved 760 characters {"type":"FeatureColl
Retrieving https://py4e-data.dr-chuck.net/
opengeo?q=Banaras+Hindu+University
Retrieved 866 characters {"type":"FeatureColl
```

- The _geoload.py_ program can be stopped at any time, and there is a counter that you can use to limit the number of calls to the geocoding API each run.

Once you have some data loaded into _geodata.sqlite_, you can visualize the data using the _geodump.py_ program.

- This program reads the database and writes the file _where.js_ with the location, latitude, and longitude in the form of executable JavaScript code.

A run of _geodump.py_ is as follows:

```python
AGH University of Science and Technology, Czarnowiejska,
Czarna Wieś, Krowodrza, Kraków, Lesser Poland
Voivodeship, 31-126, Poland 50.0657 19.91895
Academy of Fine Arts, Krakowskie Przedmieście,
Northern Śródmieście, Śródmieście, Warsaw, Masovian
Voivodeship, 00-046, Poland 52.239 21.0155
...
260 lines were written to where.js
Open the where.html file in a web browser to view the data.
The file where.html consists of HTML and JavaScript to visualize a Google map.
It reads the most recent data in where.js to get the data to be visualized. Here is
the format of the where.js file:
myData = [
[50.0657,19.91895,
'AGH University of Science and Technology, Czarnowiejska,
Czarna Wieś, Krowodrza, Kraków, Lesser Poland
Voivodeship, 31-126, Poland '],
[52.239,21.0155,
'Academy of Fine Arts, Krakowskie Przedmieściee,
Śródmieście Północne, Śródmieście, Warsaw,
Masovian Voivodeship, 00-046, Poland'],
];
```

- This is a JavaScript variable that contains a list of lists.
- The syntax for JavaScript list constants is very similar to Python.

- To see _where.html_ in the browser type `open where.html` in the terminal.
