import datetime
from dateutil.tz import tzlocal
import locale
import mail

locale.setlocale(locale.LC_TIME, "de_DE")


def print_timedelta(timedelta):
    if input == "unkown":
        return input
    days = timedelta.days
    hours = int(timedelta.seconds / 3600)
    output = str(days) + " Tag(e)" # und " + str(hours) + " Stunde(n)"
    return output


def print_date(input):
    if input is "unknown":
        return input

    # Auf eigene Zeitzone (des Servers)
    local = input.astimezone(tzlocal())

    date = datetime.datetime.strftime(local, "%d. %B %Y, %H:%M") + " Uhr"
    return date


def worker_stdout(nodes):
    # Knotenliste abarbeiten
    # Alles was > 1 Tag offline ist über Konsole ausgeben
    one_day = datetime.timedelta(days=1)
    for key,value in nodes.items():
        if value["enabled"] is False:
            continue

        timedelta = value["timedelta"]
        lastseen = value["lastseen"]
        # Fehlerfall, wenn Knoten nicht in Datenbank steht.

        # Output über Konsole
        if type(timedelta) is str or timedelta > one_day:
            hostname = value["hostname"]
            id = key
            print(id + ": Knoten offline.")
            # Weitere Infos drucken, wenn vorhanden
            if type(timedelta) is not str:
                print(id + ": " + hostname + " seit " + print_timedelta(timedelta) + " offline. (" + print_date(lastseen) + ")")
            print()  # NewLine

def worker_mail(nodes,keeper):
    # Knotenliste abarbeiten
    one_day = datetime.timedelta(days=1)
    keeper_name=keeper["name"]
    keeper_mail = keeper["address"]
    for key,value in nodes.items():
        if value["enabled"] is False:
            continue

        timedelta = value["timedelta"]
        if type(timedelta) is str:
            # Fehlerfall, wenn Knoten nicht in Datenbank steht.
            # Keine Daten vorhanden, abbruch
            continue
        lastseen = value["lastseen"]

        notify = test_for_notify_at_day(timedelta,value["notify_at_day"])

        # Output über Konsole
        if notify:
            hostname = value["hostname"]
            id = key
            # Sende Mail(s)
            for addr in value["addresses"]:
                subject=mail.createMailSubject(hostname)
                text=mail.createMailText(hostname, print_timedelta(timedelta),print_date(lastseen), keeper_mail, keeper_name)
                print(hostname+ ": Send Mail to " + addr + ". " + str(timedelta.days) +" day(s) offline.")
                #mail.sendMail(addr,subject,text)

def test_for_notify_at_day(timedelta,list_of_days):
    day_offline = timedelta.days
    for day in list_of_days:
        if day==day_offline:
            return True
    return False