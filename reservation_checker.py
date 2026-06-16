import urllib.request
import json
from datetime import timezone,timedelta,datetime

def get_available_slots():

  url = "https://license-test-tokyo-prd-police-pref-api.tokyo-madoguchi-yoyaku.com/calgetres?date=202606&coursecode=11&placecode=250&user=pub"

  JST = timezone(timedelta(hours=9))
  today_jst = datetime.now(JST)
  formatted_date = today_jst.strftime('%Y%m%d')
  print (formatted_date)

  available_slots = []

  with urllib.request.urlopen(url) as response:
    if response.status == 200:
      data = json.loads(response.read().decode("unicode-escape"))

  for slot in data['body']:
    if int(formatted_date) - int(slot["date"]) > 0: continue
    if int(slot["capacity"])-int(slot["reservation"]) > 0:
      available_slots.append({"date": slot["date"], "time": slot["starttime"]})
    
  print (available_slots)
  return available_slots