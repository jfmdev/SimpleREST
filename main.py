import datetime
import json
import uuid
from pprint import pprint
from flask import Flask, render_template, jsonify, send_from_directory, request
app = Flask(__name__, static_url_path='')

# Define main route.
@app.route("/")
def main():
    return render_template('index.html')

# Define ping service.
@app.route("/ping")
def isAlive():
    return jsonify(success=True, data="pong")

# Define timestamp service.
@app.route("/timestamp")
def getTimestamp():
    now = datetime.datetime.today()
    return jsonify(success=True, data=now)

# Define UUID service.
@app.route("/uuid")
def generateGuid():
    guid = uuid.uuid4()
    return jsonify(success=True, data=str(guid))

# Define hello service.
@app.route("/hello", methods=['POST'])
def hello():
    content = request.get_json(silent=True)
    msg = "Hello " + content['name'] + "!"
    return jsonify(success=True, data=msg)

# Define multiply service.
@app.route("/multiply", methods=['POST'])
def multiply():
    content = request.get_json(silent=True)
    result = content['num1'] * content['num2']
    return jsonify(success=True, data=result)

# Server static files.
@app.route('/lib/<path:path>')
def send_js(path):
    return send_from_directory('static', path)
    
# Execute app.
if __name__ == "__main__":
    app.debug = True
    app.run()
