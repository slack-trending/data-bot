# import websocket
from slacker import Slacker

token = 'xoxb-2215363152176-2191739510258-6GPWSiG5NONKmJZhg0FoPGn7'
slack = Slacker(token)

slack.chat.post_message('#searching-trends', 'just test')