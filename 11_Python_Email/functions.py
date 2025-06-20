import ezgmail
import os
from pathlib import Path


os.chdir(Path.home() / Path("Desktop", "Python_2024_2025", "2Practical_Applications_Using_Python", "11_Python_Email"))
ezgmail.init(credentialsFile='credentials.json')


print(ezgmail.EMAIL_ADDRESS)


ezgmail.send("amirdwikat@gmail.com", "The Title", "The context , hello this is an email sent from python")


recent_massages = ezgmail.recent()
#ezgmail.summary(recent_massages)
print(len(recent_massages))
print(recent_massages[0])
print(recent_massages[0].messages[0])
print(recent_massages[0].messages[0].subject)
print(recent_massages[0].messages[0].body)
print(recent_massages[0].messages[0].timestamp)
print(recent_massages[0].messages[0].sender)
print(recent_massages[0].messages[0].recipient)

unread_massages = ezgmail.unread()
#ezgmail.summary(unread_massages)
print(len(unread_massages))
print(unread_massages[0])
print(unread_massages[0].messages[0])
print(unread_massages[0].messages[0].subject)
print(unread_massages[0].messages[0].body)
print(unread_massages[0].messages[0].timestamp)
print(unread_massages[0].messages[0].sender)
print(unread_massages[0].messages[0].recipient)

The_Search = ezgmail.search("amir")




