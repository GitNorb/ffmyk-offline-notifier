import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import input

def sendMail(to,subject,emailText):
    # Userdaten einlesen
    userdata = input.get_json_from_local("mailsecret.json")
    password=userdata["password"]
    username=userdata["username"]

    senderEmail = username
    empfangsEmail = "nhservice@mailbox.org"
    msg = MIMEMultipart()
    msg['From'] = senderEmail
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(emailText, 'html'))

    server = smtplib.SMTP('mail.gmx.net', 587) # Die Server Daten
    server.starttls()
    server.login(senderEmail, password) # Das Passwort
    text = msg.as_string()
    server.sendmail(senderEmail, empfangsEmail, text)
    server.quit()

def createMailText(hostname, timedelta_days,lastseen, keeper_mail, keeper_name):
    hello=createTxtHello(hostname,timedelta_days,lastseen)
    firstaid=createTxtFirstAid()
    contact=createTxtContact(keeper_mail)
    bye=createTxtBye(keeper_name)
    return (hello+firstaid+contact+bye)

def createMailSubject(name_of_node):
    return "Automatische Benachrichtigung: Frifunk Knoten " + name_of_node + " offline"

def createTxtHello(hostname, timedelta_days, lastseen):
    return ("Hallo,<br><br>Ihr Router "+hostname+" ist seit "+str(timedelta_days)+" Tagen, also seit dem "+str(lastseen)+" offline.<br><br>")

def createTxtFirstAid():
    return("Meistens hilft es, wenn Sie den Router 1x vom Strom trennen und wieder einstecken. Er startet dann neu.<br><br>")

def createTxtContact(mail):
    return("Sollte das nicht funktionieren oder wollen Sie diese automatisch generierten Mails nicht mehr erhalten, benachrichtigen Sie bitte "+mail+ ".<br><br>")

def createTxtBye(name):
    return("Antworten Sie nicht an die Adresse, von der aus diese eMail gesendet wurde. Die Mail würde nicht gelesen werden.<br><br>Mit freundlichen Grüßen<br>Das Monitoringskript (von "+name +")")
