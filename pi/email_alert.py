import requests

def send_message(msg):
    return requests.post("https://api.mailgun.net/v3/sandboxd0bcfb1eddab4ba3b3567d2ad91d65d6.mailgun.org/messages",auth=("api", "e97f0039bd05466a5b3b8ff649193dd1-39bc661a-31cf3c14"),data={"from": "Project IFP <mailgun@sandboxd0bcfb1eddab4ba3b3567d2ad91d65d6.mailgun.org>","to":["dbsnuffles@gmail.com"],"subject": "Security assessment report","text": msg})


