#!/usr/bin/env python

import smtplib

smtp_server = "smtp.gmail.com"
port = 587

mail = smtplib.SMTP(smtp_server,port)
mail.starttls()

mail.ehlo()

sender = "hasankaratoyuk2@gmail.com"
password = input("Enter Gmail Password for Send Message-->")

mail.login(sender,password)

mail.sendmail(sender,"hkaratyk@gmail.com","test test")