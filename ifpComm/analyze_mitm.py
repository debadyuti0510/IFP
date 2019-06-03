import os
import json
import pprint
import requests
path = os.getcwd() + "/check_mitm/"
files = os.listdir(path)

def remove_jsons():
    for f in files:
        os.remove(path + f)

def analyze():
    unique_arps = set()
    json_objs = list()
    for filename in files:
        f = open(path + filename,"r")
        json_objs.append(json.loads(f.read()))
        f.close()
    for i in json_objs:
        for arp in i:
             unique_arps.add(json.dumps(arp))
    list_arps = list()
    for i in unique_arps:
        list_arps.append(json.loads(i))
    ip = set()
    mac = set()
    for i in list_arps:
        for j in list_arps:
            if i["ip"] == j["ip"] and i["mac"] is not j["mac"]:
                ip.add(i["ip"])
                mac.add(i["mac"]) 
    count = list()
    for i in ip:
        for j in mac:
            flag = 0
            for f in json_objs:
                for k in f:
                    if j == k["mac"] and i == k["ip"]:
                        flag = flag + 1
            count.append(flag)
    mac = list(mac)
    mitm = mac[count.index(max(count))]
    mitm_details = find_mac(mitm)
    company = mitm_details["result"]["company"]
    print("The "+company+" device with mac: " + mitm + " is the possible man in the middle.")
    remove_jsons()

def find_mac(mac):
    MAC_URL = 'http://macvendors.co/api/%s'
    r = requests.get(MAC_URL % mac)
    return r.json()

analyze()
