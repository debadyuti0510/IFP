import os
import subprocess
import json

def cmd(ip = "127.0.0.1"):
    out = subprocess.Popen(['nmap', '-F', ip],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    stdout = stdout.decode("utf-8")
    return format_report(stdout)

def format_report(nmap_cache):
    nmap_list = nmap_cache.split("\n")
    nmap_list.pop()
    report_list = list()
    nmap_list = nmap_list[5:-3]
    for service in nmap_list:
        report_dict = dict()
        information = service.split(" ")
        information = list([i for i in information if i is not ''])
        report_dict["port"] = information[0]
        report_dict["state"] = information[1]
        report_dict["service"] = information[2]
        report_list.append(report_dict)
    return report_list

def host_discovery(local_ip = '192.168.0.1/24'):
    out = subprocess.Popen(['nmap', '-sP', local_ip],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    stdout = stdout.decode("utf-8")
    lines = stdout.split('\n')
    list_ip = []
    del lines[0]
    del lines[-1]
    for line in lines[::3]:
        list_ip.append(line.split(" ")[-1])
    return list_ip

def scan_report():
    path = os.getcwd()
    path = path + "/nmap_scans"
    os.mkdir(path)
    host_list = host_discovery()
    for i in host_list:
        reports = cmd(str(i))
        if reports:
            f = open(path+ "/" +i + ".json", "w")
            for report in reports:
                r = json.dumps(report)
                f.write(str(report))
            f.close()

if __name__ == "__main__":
    scan_report()
    
