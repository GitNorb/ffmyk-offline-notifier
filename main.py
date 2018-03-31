#!/bin/python
import urllib.request
from dateutil.parser import parse
import datetime
import json

# nichts: Nur Status
# --mail: Schicke Mail

# Lese Daten ein
# A) Nodes, die beobachtet werden (nodelist.json)
# B) Alle Nodes (data)

# Extrahiere Daten, füge dabei "lastseen" hinzu
# Iteriere über nodelist, mache Output und schicke Mails wo nötig

# Lese json ein
with urllib.request.urlopen('https://map.freifunk-myk.de/hopglass/nodes.json') as url:
    data = json.loads(url.read().decode())
# Lese Nodeliste ein
nodelist_json = json.load(open('nodelist.json'))

# Extrahiere lastseen
lastseen_list = {}
hostname_list = {}
for n in data["nodes"]:
    id=n["nodeinfo"]["node_id"]
    hostname=n["nodeinfo"]["hostname"]
    lastseen=n["lastseen"]
    dt = parse(lastseen)

    lastseen_list[id]=dt
    hostname_list[id]=hostname

for n in nodelist_json["nodes"]:
    id=n["id"]
    hostname=hostname_list[id]
    lastseen=lastseen_list[id]
    n["lastseen"]=lastseen
    n["hostname"]=hostname

# Knotenliste abarbeiten
now = datetime.datetime.now(datetime.timezone.utc)
one_day = datetime.timedelta(days=1)

for n in nodelist_json["nodes"]:
    lastseen=n["lastseen"]
    timedelta = now-lastseen
    if timedelta > one_day:
        id=n["id"]
        hostname=n["hostname"]
        owner=n["owner"]
        address=n["address"]
        print("Knoten " + hostname +" seit " + str(lastseen) + " offline. Besitzer ist " + owner)



