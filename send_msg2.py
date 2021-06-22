import logging

from flask.wrappers import Response
logging.basicConfig(level=logging.DEBUG)

import os
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError

slack_token = os.environ['SLACK_BOT_TOKEN']
client = WebClient(token=slack_token)

try:
    response = client.chat_postMessage(
        channel="searching-trends",
        text = "ssibal"
    )   

except SlackApiError as e:
    assert e.response['error']


