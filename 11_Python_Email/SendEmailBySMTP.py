import smtplib


sender_email = 'amirdwikat@example.com'
recipient_email = 'amirdwikat@example.com'
password = "lcpc rowl eyzd jpxl"
massage = "Hello this is massage from py , sent by SMTP"


server = smtplib.SMTP("smtp.example.com", 587)
server.starttls()
server.login(sender_email, password=password)
print("Login success")
server.sendmail(sender_email, recipient_email, massage)
print(f"The email has been sent to {recipient_email}.")
server.quit()



