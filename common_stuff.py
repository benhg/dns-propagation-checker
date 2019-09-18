import urllib.request
from urllib.error import HTTPError, URLError
from socket import timeout

slack_webhook_link = "https://hooks.slack.com/services/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"

def get_status(service, to=3):
    try:
        response = urllib.request.urlopen(service, timeout=to).getcode()
    except (HTTPError, URLError) as error:
        return 'down'
    except timeout:
        return 'down'
    else:
        if response == 200:
            return 'up'
        else:
            return 'down'

svc_list = {
    "Datasci Jupyter": "https://jupyter.datasci.watzek.cloud",
    "Datasci Home": "https://datasci.watzek.cloud",
    "Datasci RStudio": "https://rstudio.datasci.watzek.cloud",
    "EZProxy": "https://library.lcproxy.org",
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
    "LC PhysX": "https://lcphysx.lclark.edu"
    }
