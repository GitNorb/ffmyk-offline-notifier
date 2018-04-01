import datetime
from dateutil.tz import tzlocal
import locale

locale.setlocale(locale.LC_TIME, "de_DE")


def pretty_print_timedelta(timedelta):
    if input == "unkown":
        return input
    days = timedelta.days
    hours = int(timedelta.seconds / 3600)
    output = str(days) + " Tag(e) und " + str(hours) + " Stunde(n)."
    return output


def pretty_print_date(input):
    if input is "unknown":
        return input

    # Auf eigene Zeitzone (des Servers)
    local = input.astimezone(tzlocal())

    date = datetime.datetime.strftime(local, "%d. %B %Y")
    return date


def worker(nodes):
    # Knotenliste abarbeiten
    one_day = datetime.timedelta(days=1)
    for n in nodes:
        if n["enabled"] is False:
            continue

        timedelta = n["timedelta"]
        lastseen = n["lastseen"]
        # Fehlerfall, wenn Knoten nicht in Datenbank steht.

        # Output über Konsole
        if type(timedelta) is str or timedelta > one_day:
            hostname = n["hostname"]
            id = n["id"]
            print(id + ": Knoten offline.")
            if type(timedelta) is not str:
                print(id + ": " + hostname + " seit dem " + pretty_print_date(
                    lastseen) + " offline. " + pretty_print_timedelta(timedelta))
                # Sende Mail(s)
                # TODO Erstelle Mail aus Template in /tmp/offline_notify_mailXXXX.txt
                for a in n["adresses"]:
                    i=0
                    # TODO mail -s "hostname offline" a < /tmp/offline_notify_mailXXXX.txt
                    # TODO delete /tmp/offline_notify_mailXXXX.txt
            print()  # NewLine
