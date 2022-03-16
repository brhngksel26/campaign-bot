


token = "xoxb-3232191403175-3270567506144-AA5GWD9VcXvF6rTqm1IFwI2a"

from slack_sdk import WebClient
import os
from pathlib import Path



client = WebClient(token=token)

client.chat_postMessage(channel="#campaign",text="hello")


