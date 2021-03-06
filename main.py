#!/bin/python
import input
import process
import output
import sys

# Parameter:
# nichts: Nur Status
# --mail: Schicke Mail

# Lese Daten ein
# A) Nodes, die beobachtet werden (nodelist.json)
# B) Alle Nodes (data)

if "nomail" in sys.argv:
    nomail=True
    print("Simuliere... sende keine Mail")

# Input: Die beiden JSON
data = input.get_json_from_url('https://map.freifunk-myk.de/hopglass/nodes.json')
nodelist_json = input.get_json_from_local('nodelist.json')
# Extrahiere lastseen und hostname und führe zusammen
lastseen_list, hostname_list = process.extract_hostname_and_lastseen(data["nodes"])
nodelist_json = process.merge_data(nodelist_json, hostname_list, lastseen_list)
# TODO: Sortieren nach Timedelta

# Output auf Konsole und bei Bedarf Mail
output.worker_stdout(nodelist_json["nodes"])
process.test_sites(data["nodes"])
output.worker_mail(nodelist_json["nodes"], nodelist_json["keeper"],nomail)
