import smtplib
import datetime as dt
import pandas as pd



now = dt.datetime.now().weekday()

if now == 0:
    data = pd.read_fwf('quotes/quotes.txt')
    daily_motivation = data.sample().values[0][0]
    my_password = "1bCd3$g7"
    my_email = "test@yahoo.com"

    connection = smtplib.SMTP("smtp.mail.yahoo.com")
    connection.starttls()
    connection.login(user = my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="mytestemail@gmail.com",
        msg=f"Subject:Quote of the day\n\n{daily_motivation}")
    connection.close()
else:
    print("Today is not monday!")