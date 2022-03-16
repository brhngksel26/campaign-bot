from slack_sdk import WebClient
from slackeventsapi import SlackEventAdapter

token = "xoxb-3232191403175-3270567506144-Oh7ALqR6c58Rj5Ca1wLrov7W"
signing_secret = "2f47b4f69fc6cc41ab0a8d99794176c7"

channel_name = "campaign"
client = WebClient(token=token)
conversation_id = None

def getChannelId():
    for result in client.conversations_list():
        if conversation_id is not None:
            break
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                conversation_id = channel["id"]
                    #Print result
                print(f"Found conversation ID: {conversation_id}")
                break


def sendMessage(message):
    client.chat_postMessage(channel="#campaign",text=message)


sendMessage("hello")