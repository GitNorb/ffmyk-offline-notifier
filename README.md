# ffmyk-offline-notifier
Freifunk-MYK, sendet Mails, wenn Knoten offline

# Funktion
Erst wird die Datenbank (2-3 MB, .json) vom Kartenserver geladen.
Danach wird die Liste mit den Informationen über die zu beobachtenden Knoten eingelesen.
Die benötigten Daten werden aus der Datenbank entnommen und den Informationen zu den Knoten hinzugefügt.
Zuletzt wird über die zu beobachtenden Knoten iteriert und bei Bedarf Mails versendet.

# Begriffe
Keeper: Der Admin, der sich um die Knoten kümmert

# 
