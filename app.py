from flask import Flask, render_template
import requests

import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import json

from common_stuff import get_status
from common_stuff import svc_list

app = Flask(__name__)

app.config["admin_email"] = "benjamin.glick@ge.com"
app.secret_key = b'\x9b4\xf8%\x1b\x90\x0e[?\xbd\x14\x7fS\x1c\xe7Y\xd8\x1c\xf9\xda\xb0K=\xba'
# I will obviously change this secret key before we go live

slack_webhook_link = "https://hooks.slack.com/services/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"

@app.route('/')
@app.route('/index')
@app.route('/index.html')
@app.route('/index.php')
@app.route('/home')
@app.route('/home.html')
@app.route('/login')
@app.route('/status')
def hello_world():
    """Home Page"""
    status = {}
    for service in svc_list.keys():
        status[service] = get_status(svc_list[service])

    return render_template("status.html", status=status)

@app.route("/status_update", methods=["GET", "POST"])
def status_breakdown():
    for service in svc_list.keys():
        status = get_status(svc_list[service])
        message = "Service '{}' is currently {}. Check URL {} for more info".format(service, status, svc_list[service])
        requests.post(slack_webhook_link, headers={'Content-type': 'application/json'}, data=json.dumps({"text": message}))
    return ""






