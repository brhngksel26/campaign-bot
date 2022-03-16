from slack_sdk import WebClient


token = "xoxb-3232191403175-3270567506144-Oh7ALqR6c58Rj5Ca1wLrov7W"

client = WebClient(token=token)




def main():
    channel_name = "campaign"
    conversation_id = None
    for result in client.conversations_list():
        if conversation_id is not None:
            break
        for channel in result["channels"]:
            if channel["name"] == channel_name:
                conversation_id = channel["id"]
                #Print result
                print(f"Found conversation ID: {conversation_id}")
                break
   
def read():
    result = client.conversations_history(
        channel="C037B3Z5Y20",
        inclusive=True,
        oldest="1610144875.000600",
        limit=1
    )

    message = result["messages"][0]
    # Print message text
    print(message["text"])

if __name__ == '__main__':
    read()