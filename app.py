from flask import Flask, render_template

import os
import socket
import subprocess

app = Flask(__name__)

app.config["admin_email"] = "benjamin.glick@ge.com"
app.secret_key = b'\x9b4\xf8%\x1b\x90\x0e[?\xbd\x14\x7fS\x1c\xe7Y\xd8\x1c\xf9\xda\xb0K=\xba'
# I will obviously change this secret key before we go live

nodes_list = ["mayo", "bacon", "lettuce", "tomato", "sprouts"]
services_list = ["dns", "ping", "ssh", "sge"]
os.environ["SGE_ROOT"] = '/local/cluster/sge'


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
    for node in nodes_list:
        status[node] = {}
        for service in services_list:
            status[node][service] = get_status(node, service)

    return render_template("status.html", status=status)


def get_status(node, service):
    if node == "mayo":
        return "up"
    if service == "ping":
        if ping_return_code(node) == 0:
            return "up"
        return "down"
    elif service == "dns":
        try:
            socket.gethostbyname(node)
            return 'up'
        except socket.error:
            return 'down'
    elif service == 'ssh':
        return "up"
    elif service == "sge":
        status_message = os.popen(
            "qping -info {} 6445 execd 1".format(node)).read()
        for line in status_message.split("\n"):
            if "status:" in line:
                if "0" in line:
                    return "up"
        return "down"


def ping_return_code(hostname):
    """Use the ping utility to attempt to reach the host. We send 5 packets
    ('-c 5') and wait 3 milliseconds ('-W 3') for a response. The function
    returns the return code from the ping utility.
    """
    ret_code = subprocess.call(['ping', '-c', '1', '-W', '2', hostname],
                               stdout=open(os.devnull, 'w'),
                               stderr=open(os.devnull, 'w'))
    return ret_code
