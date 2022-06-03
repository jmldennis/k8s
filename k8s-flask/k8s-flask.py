from flask import Flask, request

#Initialize Flask App
app = Flask(__name__)
port = 5005

@app.route('/', methods=['GET'])
def index():
    """Receive a notification from Webex Teams and handle it"""
    if request.method == 'GET':
        return f'Request received on local port {port}'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)