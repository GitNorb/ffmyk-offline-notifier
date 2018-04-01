# Process-Stuff


from dateutil.parser import parse
import datetime

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