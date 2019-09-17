from flask import Flask, render_template

import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import requests
import json

app = Flask(__name__)

app.config["admin_email"] = "benjamin.glick@ge.com"
app.secret_key = b'\x9b4\xf8%\x1b\x90\x0e[?\xbd\x14\x7fS\x1c\xe7Y\xd8\x1c\xf9\xda\xb0K=\xba'
# I will obviously change this secret key before we go live

slack_webhook_link = "https://hooks.slack.com/services/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"


svc_list = {
    "jupyter": "https://jupyter.datasci.watzek.cloud",
    "Datasci Home": "https://datasci.watzek.cloud",
    "Datasci RStudio": "https://rstudio.datasci.watzek.cloud",
    "ezproxy": "https://library.lcproxy.org",
    "William Stafford Archive":"http://williamstaffordarchives.org",
    "AccessCeramics": "http://accessceramics.org",
    "Oregon Poetic Voices": "http://oregonpoeticvoices.org",
    "Watzek Server (watzek.lclark.edu)": "https://watzek.lclark.edu",
    "Library Homepage (library.lclark.edu)": "https://library.lclark.edu",
    "Vietnam Project": "https://vietnam.watzekdi.net",
    "Senior Projects":"https://watzek.lclark.edu/seniorprojects/",
    "LC Collaborative Research": "http://collaborativeresearch.lclark.edu",
    "Special Collections": "http://specialcollections.lclark.edu",
    "DataViz Server": "https://viz.datasci.watzek.cloud",
    "TEST_nonrespond":"http://TEST_nonrespond.biz.ru",
    "TEST_500error":"http://httpstat.us/500",
    "TEST_404error":"http://httpstat.us/404",
    }


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


def get_status(service):
    try:
        response = urllib.request.urlopen(service, timeout=1).getcode()
    except (HTTPError, URLError) as error:
        return 'down'
    except timeout:
        return 'down'
    else:
        if response == 200:
            return 'up'
        else:
            return 'down'






