#!/usr/local/bin/env python3

import json

import requests

from common_stuff import get_status, svc_list

slack_webhook_link = "https://hooks.slack.com/services/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"


def check_statuses():
    """Home Page"""
    status = {}
    for service in svc_list.keys():
        if get_status(svc_list[service]) == 'down':
            message = "Service '{}' is currently Down. Check URL: {}.".format(service, svc_list[service])
            requests.post(slack_webhook_link, headers={'Content-type': 'application/json'}, data=json.dumps({"text": message}))


if __name__ == '__main__':
    check_statuses()




