import requests

api = ""
domain = ""

with open("api.txt","r") as f:
    api = f.read()
    f.close()
with open("domain.txt","r") as f:
    domain = f.read()
    f.close()

def send_message(msg):
    return requests.post(domain,auth=("api", api),data={"from": "Project IFP <mailgun@"+ domain  +">","to":["dbsnuffles@gmail.com"],"subject": "Security assessment report","text": msg})

if __name__ == "__main__":
    print(api + " " + domain)
