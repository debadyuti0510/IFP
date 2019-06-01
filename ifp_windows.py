import os
import subprocess

def cmd_to_string():
    out = subprocess.Popen(['arp', '-a'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    stdout,stderr = out.communicate()
    stdout = stdout.decode("utf-8")
    return stdout

def format_report():
    arp_list = arp_cache.split("\n")
    arp_list = arp_list[3:-1]
    report_list = list()
    for element in arp_list:
        report_dict = dict()
        unit = element.split(" ")
        new_unit = list()
        for i in unit:
            if(i):
                new_unit.append(i)
        report_dict["ip"] = new_unit[0]
        report_dict["mac"] = new_unit[1]
        report_list.append(report_dict)
    print(report_list)

if __name__ == "__main__":
    arp_cache = cmd_to_string()
    print(arp_cache)
    arp_list = format_report()
    print(arp_list)

     
