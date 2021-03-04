
# TO RUN YOUR CODE:
# https://www.pythonanywhere.com/


import datetime as dt
import pandas
import smtplib
import random
PLACEHOLDER = "[NAME]"

my_email = "xxxxxxxx@gmail.com"
password = "xxxxxxxx"

# CHECKING A DAY AND A MONTH TODAY:
today = dt.datetime.now()
today_tuple = (today.month, today.day)

# READING CSV as DataFrame:
data = pandas.read_csv("birthdays.csv")

# CREATING A DICTIONARY:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }

# we want our dictionary to look like:
# birthdays_dict = {
#     (12, 25): Mama,laramera@outlook.it,1961,3,3
# }

# Dictionary comprehension template for pandas DataFrame looks like this:
# we can use a method iterrows() to iterate through our DataFrame called data
# then we got index of each of those rows (index) and also the data in each of these rows(data_row)
# and then we crete a new dictionary with a new key (data_row["month"]) and a new value: : data_row
# from all rows that we iterated through
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# If today's month and day exists in a tuple of our dictionary:
if today_tuple in birthdays_dict:
    # we are getting a row from dict that matches today's month and day
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # SENDING A LETTER:
    # creating a connection:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # calling to starttls:
        connection.starttls()
        # logging to our connection:
        connection.login(my_email, password)
        # setting up the subject and the content:
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )









