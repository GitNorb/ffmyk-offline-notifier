import datetime


def worker(nodes):
    # Knotenliste abarbeiten
    now = datetime.datetime.now(datetime.timezone.utc)
    one_day = datetime.timedelta(days=1)
    for n in nodes:
        if n["enabled"] is False:
            continue
        lastseen = n["lastseen"]
        # Fehlerfall, wenn Knoten nicht in Datenbank steht.
        if lastseen != "unknown":
            timedelta = now - lastseen
        else:
            timedelta == "unknown"
        if timedelta > one_day:
            id = n["id"]
            hostname = n["hostname"]
            address = n["addresses"]
            print("Knoten " + hostname + " seit " + str(lastseen) + " offline.")


