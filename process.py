# Process-Stuff


from dateutil.parser import parse
import datetime
import sys

def merge_data(nodelist_json, hostname_map, lastseen_map):
    for key,value in nodelist_json["nodes"].items():
        id = key
        try:
            hostname = hostname_map[id]
            lastseen = lastseen_map[id]
            timedelta = datetime.datetime.now(datetime.timezone.utc) - lastseen
        except KeyError:
            # Wenn Knoten zu lange offline sind, verschinden sie von der Karte.
            # Sie stehen dann nicht mehr in der Datenbank.
            # Wird hier abgefangen.
            # print('I got a KeyError for id "%s"' % str(id))
            lastseen = "unknown"
            timedelta = "unknown"
            hostname = "unknown"

        value["timedelta"] = timedelta
        value["lastseen"] = lastseen
        value["hostname"] = hostname
    return nodelist_json

def extract_hostname_and_lastseen(nodelist):
    lastseen_map = {}
    hostname_map = {}
    for n in nodelist:
        id = n["nodeinfo"]["node_id"]
        hostname = n["nodeinfo"]["hostname"]
        lastseen = n["lastseen"]
        dt = parse(lastseen)

        lastseen_map[id] = dt
        hostname_map[id] = hostname
    return lastseen_map, hostname_map

# Zähle wie viele Knoten einer Sites online/offline sind, um Probleme mit der Karte aufzudecken



def test_sites(nodes):
    sites = {}
    for node in nodes:
        online = node["flags"]["online"]
        site = node["nodeinfo"]["system"]["site_code"]
        if not (site in sites):
            sites[site]={"online":0,"offline":0}
        if online:
            sites[site]["online"]=sites[site]["online"]+1
        else:
            sites[site]["offline"] = sites[site]["offline"] + 1
    offline_sites=[]
    for key,value in sites.items():
        online = value["online"]
        offline = value["offline"]
        proportion = online/(offline+online)
        if proportion < 0.5:
            offline_sites.append(key)
            print(key + " ist mehrstens offline!")
    if len(offline_sites)>1:
        print("Abbruch wegen offline Sites!")
        sys.exit(1)