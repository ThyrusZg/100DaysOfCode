##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

# ------------------------- IMPORTS -------------------------
import pandas as pd
import datetime as dt
import random
import smtplib
PLACEHOLDER = "[NAME]"

def check_birthday():
    today = dt.datetime.now()
    birthdays = pd.read_csv("birthdays.csv")
    for index, row in birthdays.iterrows():
        if row['month'] == today.month and row['day'] == today.day:
            return row
    return None

def pick_and_write_letter(name):
    letter_number = random.randint(1,3)
    with open(f"letters/letter_{letter_number}.txt", "r") as letter:
        letter_content = letter.readlines()

    with open(f"letters/letter_{letter_number}.txt", "w") as output:
        pre_name = letter_content[0].split(" ")[0]
        name = letter_content[0].split(" ")[1].replace(PLACEHOLDER, name)
        line = pre_name + " " + name
        output.write(line + "".join(letter_content[1:]))

    with open(f"letters/letter_{letter_number}.txt", "r") as letter:
        final_content = letter.readlines()

    return final_content

def send_email(message,email):
    my_password = "1bCd3$g7"
    my_email = "test@yahoo.com"

    connection = smtplib.SMTP("smtp.mail.yahoo.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs=email,
        msg=f"Subject:Happy birthday\n\n{message}")
    connection.close()


person = check_birthday()

if person is not None:
    letter = pick_and_write_letter(person["name"])
    send_email(letter, person["email"])
else:
    print("No birthday today!")






