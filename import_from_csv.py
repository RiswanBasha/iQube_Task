'''
This task deals with recieving a mail from the defined user when the current date matches with the given CSV file's date
and Body of the mail will be the attachments of the particular date.
'''

#importing some modeules for this particular task
import sqlite3,csv
import os
import smtplib
import imghdr
from datetime import date
from email.message import EmailMessage

#I have got the current date 
today = date.today()

# dd/mm/YY
d1 = today.strftime("%d-%m-%Y")
print(d1)

# This is the requirement code for connecting python with sqlite3 Database
connection = sqlite3.connect("csv.db")
cursor = connection.cursor()

#This process will get my CSV file as an input and inserted into the table which I have already created 
with open('task.csv','r+') as file:
    track=0
    for row in file:
        cursor.execute("INSERt INTO CsvTable VALUES (?,?,?)" ,row.split(','))
        connection.commit()
        #This track is just to make sure the count of my csv file , This is not necessary
        track+=1


connection.close()
#So, finally my CSV file will be reflected in my DB whenever I update or Run. I have inserted my csv in a DB just to store without any revoking. 
print("\n{} : Tacks ".format(track))


# This email credential is hidden since, I have updated my credential in my environmental varibales. This kind of securities is very much used in Big projects.
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")


#This Emailmessage is a module in which we can give our credentials with subject ,from address , To address
msg = EmailMessage()
msg['Subject'] = 'Task Working Successfully'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'riswan.17ec@kct.ac.in'

#This is the final part of this task. I have iterated my csv file with the current date , If it matches , Then the current date's attachment will be sent as mail.
with open('task.csv') as file:
    contacts=csv.DictReader(file)
    for contact in contacts:
        #if the current date matches with the given csv date then it performs the below operation
        if contact['Date']==d1:
            msg.set_content( contact['Attachments'] )
            #this is just I'm initializing my smtp mail format and port number of this protocol
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
                smtp.send_message(msg)