#!/usr/local/bin/env python3

import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout
import json
import requests

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

def check_statuses():
    """Home Page"""
    status = {}
    for service in svc_list.keys():
        if get_status(svc_list[service]) == 'down':
            message = "Service '{}' is currently Down. Check URL: {}.".format(service, svc_list[service])
            requests.post(slack_webhook_link, headers={'Content-type': 'application/json'}, data=json.dumps({"text": message}))



def get_status(service):
    try:
        response = urllib.request.urlopen(service, timeout=3).getcode()
    except (HTTPError, URLError) as error:
        return 'down'
    except timeout:
        return 'down'
    else:
        if response == 200:
            return 'up'
        else:
            return 'down'

if __name__ == '__main__':
    check_statuses()




