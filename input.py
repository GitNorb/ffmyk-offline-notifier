# Input-Stuff

import urllib.request
import json

def get_json_from_url(url_string):
    # Lese json ein
    with urllib.request.urlopen(url_string) as url:
        data = json.loads(url.read().decode())
    return data

def get_json_from_local(local_string):
    # Lese Nodeliste ein
    nodelist_json = json.load(open(local_string))
    return nodelist_json