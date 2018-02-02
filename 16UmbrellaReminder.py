#!/usr/bin/python3
# chap16PracProjUmbrellaReminder.py
# Checks daily forecast and notifies if rain is expected.
# Weather source is OpenWeatherMap API.
# Notification is via email from Yahoo burner to personal.

import json
import requests
import smtplib
import sys

url = "http://api.openweathermap.org/data/2.5/forecast?zip=ZIP,us&APPID=yourAPPID"
weatherJSON = requests.get(url)

try:
	weatherJSON.raise_for_status()
except:
	print("Something went wrong getting the API data")
	sys.exit()
	
weatherDict = json.loads(weatherJSON.text)
todayList = []
for i in range(0, 5):
    todayList.append(weatherDict["list"][i]["weather"][0]["main"])

if "Rain" in todayList:
    smtpObj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    smtpObj.ehlo()
    smtpObj.starttls()
    smtpObj.login(input('login'), input('password'))
    smtpObj.sendmail("sender", "receiver", "Subject: Bring an Umbrella!\n\nThere's rain afoot.")
    smtpObj.quit()
else:
    print("These are the expected conditions every three hours:")
    for condition in todayList:
        print(condition)

