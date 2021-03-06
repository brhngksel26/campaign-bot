from slack_sdk import WebClient
from flask import Flask
from slackeventsapi import SlackEventAdapter
from app.mainSheets import getCampaignValue

token = "xoxb-3232191403175-3270567506144-Oh7ALqR6c58Rj5Ca1wLrov7W"
signing_secret = "2f47b4f69fc6cc41ab0a8d99794176c7"

app = Flask(__name__)


slack_event_adapter = SlackEventAdapter(signing_secret, "/slack/events", app)
client = WebClient(token=token)

BOT_ID = client.api_call('auth.test')['user_id']

@slack_event_adapter.on('reaction_added')
def getMessage(payload):
    print("asds")
    event = payload.get('event',{})
    channel_id = event.get('channel')
    user_id = event.get('user')
    text = event.get('text')
    print("asds")

    if BOT_ID != user_id:
        return client.chat_postMessage(channel="#campaign",text=text)

@app.route('/')
def index():
    client.chat_postMessage(channel="#campaign",text="text")
    return "asdasd"

@app.route("/campaign/<campaign>")
def campaign(campaign):
    campaignData = []

    if campaign.find("+") == -1:
        campaignData.append(campaign)
    else:
        campaignData = campaign.split("+")

    sheetData = getCampaignValue(campaignData)
    header = ['Campaign name', 'Total Impression', 'Total Clicks', 'CTR (%)', 'CPC', 'Total App Install']
    for data in sheetData:
        message =autoReplace(header) + "\n" + autoReplace(data)
        client.chat_postMessage(channel="#campaign",text=message)
        
    return "campaignData"

    
def autoReplace(message):
    return str(message).replace("[","").replace("'","-").replace("]","")

if __name__ == "__main__":
    app.run(debug=True)