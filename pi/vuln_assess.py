import json
import os
import shutil
from email_alert import send_message
from ifp_nmap import scan_report

if __name__ == "__main__":
    scan_report()
    message = ""
    path = os.getcwd()
    path = path + "/nmap_scans/"
    files = os.listdir(path)
    ports = list()
    for filename in files:
        if filename !='192.168.0.1.json' and filename != '192.168.1.1.json':
            with open(path + filename, encoding='utf-8') as data_file:
                ports = json.loads(data_file.read())
            services = ""
            open_ports = ""
            for port in ports:
                services = services + str(port["service"]) + ", "
                open_ports = open_ports + str(port["port"].split("/")[0]) + ", " 
            message = message + "In device with IP: " + filename.split(".json")[0] + " services " + services + "\b\b are running on ports " + open_ports + "\b\b respectively and may be vulnerable to attacks.\n\n"  
    print(message)
    shutil.rmtree(path)
