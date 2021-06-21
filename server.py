# import os
from flask import Flask
# from slack import WebClient

app = Flask(__name__)

# slack_web_client = WebClient(token = os.environ.get("SLACKBOT_TOKEN"))

@app.route("/", methods=['POST']) 
def hello_world():
    return 'Hello world'
