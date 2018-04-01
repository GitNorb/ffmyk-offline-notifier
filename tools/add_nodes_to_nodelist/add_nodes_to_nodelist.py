#!/bin/pyhton
import json

INPUT_TXT= 'nodes.txt' # neue Knoten
INPUT_JSON='nodelist.json' # alte Knoten
OUTPUT_JSON='nodelist_new.json'

# File mit den neuen Knoten öffnen
with open(INPUT_TXT) as f:
    new_nodes = f.readlines()
new_nodes_list = [x.strip() for x in new_nodes]

# File mit den alten Knoten öffnen
old_nodes_json = json.load(open(INPUT_JSON))
old_nodes = old_nodes_json["nodes"]

# KnotenMap erstellen
new_nodes_map={}
for node_new in new_nodes_list:
    # Überprüfe, ob schon vorhanden
    if node_new in old_nodes:
        node_old=old_nodes[node_new]
        # übernehme Werte
        enabled=node_old["enabled"]
        addresses=node_old["addresses"]
        notify_at_day = node_old["notify_at_day"]
    else:
        # Erstelle Standardwerte
        enabled = False
        addresses = []
        notify_after_days = [1,3,7,13]

    # Füge Knoten neuer Map hinzu
    new_nodes_map[node_new]={}
    new_nodes_map[node_new]["enabled"]=enabled
    new_nodes_map[node_new]["addresses"] = addresses
    new_nodes_map[node_new]["notify_at_day"] = notify_at_day

# Keeper erstellen
if "keeper" in old_nodes_json:
    keeper = old_nodes_json["keeper"]
else:
    keeper={}
    keeper["name"]="unkown"
    keeper["address"] = "unkown"


# Ergebnis schreiben
output_map = {}
output_map["keeper"]=keeper
output_map["nodes"]=new_nodes_map


with open(OUTPUT_JSON, 'w') as fp:
    json.dump(output_map, fp)

