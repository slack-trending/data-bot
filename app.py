# from logging import debug
from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello_world():
    return 'hello world!'

# if __name__ == '__main__':
#     app.run('0.0.0.0', port=5000, debug=True)