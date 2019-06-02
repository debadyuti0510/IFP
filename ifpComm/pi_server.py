import socket

if __name__=="__main__":
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 6789
    serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))
    while True:
        data, addr = serverSock.recvfrom(1024)
        data = data.decode("utf-8")
        data = data.split("IP: ")
        ip = data[1]
        received_data = data[0]
        f = open(ip + ".json", "w")
        f.write(received_data)
        f.close()
        print("Message: " + ip)
