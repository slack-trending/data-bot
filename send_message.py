import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2215363152176-2191739510258-6GPWSiG5NONKmJZhg0FoPGn7"
 
post_message(myToken,"#searching-trends","hi, I'm collec data bot!!")
