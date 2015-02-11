import smtplib

fromaddr = 'vaughnwatson22@gmail.com'

toaddrs = 'david@alteroo.com'

message = """From: {} <{}>

To: {} <{}>

Subject: {}

{}

"""
fromname = 'Bobby'
toname = 'David Bain'
subject = 'lab3'
msg = 'mail app working'

messagetosend = message.format(

 fromname,

 fromaddr,

 toname,

 toaddrs,

 subject,

 msg)

# Credentials (if needed)

username = 'vaughnwatson22@gmail.com'

password = 'nkftpseosltzdezn'

# The actual mail send

server = smtplib.SMTP('smtp.gmail.com:587')

server.starttls()

server.login(username,password)

server.sendmail(fromaddr, toaddrs, messagetosend)

server.quit()