from flask import Flask, render_template

import urllib.request

app = Flask(__name__)

app.config["admin_email"] = "benjamin.glick@ge.com"
app.secret_key = b'\x9b4\xf8%\x1b\x90\x0e[?\xbd\x14\x7fS\x1c\xe7Y\xd8\x1c\xf9\xda\xb0K=\xba'
# I will obviously change this secret key before we go live

svc_list = {
    "jupyter": "https://jupyter.datasci.watzek.cloud",
    "Datasci Home": "https://datasci.watzek.cloud",
    "Datasci RStudio": "https://rstudio.datasci.watzek.cloud",
    "ezproxy": "https://library.lcproxy.org",
    "William Stafford Archive":"http://williamstaffordarchives.org",
    "AccessCeramics": "http://accessceramics.org",
    "Oregon Poetic Voices": "http://oregonpoeticvoices.org"
    "Watzek Server (watzek.lclark.edu)": "https://watzek.lclark.edu",
    "Library Homepage (library.lclark.edu)": "https://library.lclark.edu",
    "Vietnam Project": "https://vietnam.watzekdi.net",
    "Senior Projects":"https://watzek.lclark.edu/seniorprojects/",
    "LC Collaborative Research": "http://collaborativeresearch.lclark.edu",
    "Special Collections": "http://specialcollections.lclark.edu",
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


def get_status(service):
    if urllib.request.urlopen(service).getcode() == 200:
        return 'up'
    else:
        return 'down'
