import json
import socket
import subprocess
from ifp_linux import cmd_to_string
import socket

target = "127.0.0.1"

if __name__ == "__main__":
    UDP_IP_ADDRESS = target
    UDP_PORT_NO = 6789
    out = subprocess.Popen(['hostname', '-I'],stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    IPAddr,stderr = out.communicate()
    IPAddr = IPAddr.decode("utf-8")
    Message = json.dumps(cmd_to_string()) + "\nIP: " + IPAddr 
    Message = bytes(Message, "utf-8")
    clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))
