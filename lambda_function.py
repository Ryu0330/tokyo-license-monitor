from reservation_checker import get_available_slots
from discord_notifier import post_discord

def lambda_handler(event, context):
  slots = get_available_slots()

  if slots:
    post_discord(slots)