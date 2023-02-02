import requests
import json
from attd import AttributeDict

def get_invite(invite_code):
  url = f"https://discord.com/api/v10/invites/" + invite_code
  response = requests.get(url)
  if response.status_code == 200:
    return (AttributeDict(response.json()))

  elif response.status_code == 404:
    return ("Invite not found")
  elif response.status_code == 429:
    return ("Too many requests")
  else:
    return ("Erorr")
    
