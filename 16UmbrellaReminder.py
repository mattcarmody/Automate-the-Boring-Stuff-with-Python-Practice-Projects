# Checks daily forecast and notifies if rain is expected.
# Weather source is OpenWeatherMap API.
# Notification is via email from Yahoo burner to personal.

import json
import requests
import smtplib
import sys

ZIP = YOUR_ZIP_CODE
APPID = YOUR_APPID
url = "http://api.openweathermap.org/data/2.5/forecast?zip={},us&APPID={}".format(ZIP, APPID)
weatherJSON = requests.get(url)

try:
	weatherJSON.raise_for_status()
except:
	print("Something went wrong getting the API data")
	sys.exit()
	
weather = json.loads(weatherJSON.text)
today = []
for i in range(0, 5):
    today.append(weather["list"][i]["weather"][0]["main"])

if "Rain" in today:
    smtp_obj = smtplib.SMTP('smtp.mail.yahoo.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(input('login'), input('password'))
    smtp_obj.sendmail("sender", "receiver", "Subject: Bring an Umbrella!\n\nThere's rain afoot.")
    smtp_obj.quit()
else:
    print("These are the expected conditions every three hours:")
    for condition in today:
        print(condition)

