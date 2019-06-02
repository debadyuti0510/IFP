import os
import subprocess

def cmd_to_string():
    out = subprocess.Popen(['arp', '-a'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    stdout = stdout.decode("utf-8")
    return format_report(stdout)

def format_report(arp_cache):
    arp_list = arp_cache.split("\n")
    arp_list.pop()
    report_list = list()
    for element in arp_list:
        report_dict = dict()
        unit = element.split(" ")
        ip = unit[1]
        ip = ip[1:-1]
        mac = unit[3]
        report_dict["ip"] = ip
        report_dict["mac"] = mac
        report_list.append(report_dict)
    return(report_list)

if __name__ == "__main__":
    print(cmd_to_string())
