import smtplib

my_password = input("Password:")
my_email = ""

connection = smtplib.SMTP("smtp.mail.yahoo.com")
connection.starttls()
connection.login(user = my_email, password=my_password)
connection.sendmail(from_addr=my_email,to_addrs="mytestemail@gmail.com", msg="Subject:Hello\n\nPy Message")
connection.close()
