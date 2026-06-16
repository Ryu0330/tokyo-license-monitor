import urllib.request
import json
import os

def post_discord(slots):

  WEBHOOK_URL = os.environ["DISCORD_WEBHOOK_URL"]

  message = (
    "本免学科試験に空きが見つかりました。\n\n場所 |  日付  |  時間\n"
    + "\n".join(
        f"{slot['place']} | {slot['date'][4:6]}/{slot['date'][6:8]} | {slot['time'][:2]}:{slot['time'][2:]}"
        for slot in slots
    )
  )
  headers = {
      "Content-Type": "application/json",
      "User-Agent": "DiscordBot (private use) Python-urllib/3.10",
  }
  data = {"content": message}
  request = urllib.request.Request(
      WEBHOOK_URL,
      data=json.dumps(data).encode(),
      headers=headers,
      method="POST"
  )

  with urllib.request.urlopen(request) as res:
      assert res.getcode() == 204