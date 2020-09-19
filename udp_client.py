#!/usr/bin/python3.6
import socket
UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = 5009
Message = "Hello, Server".encode()

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    msg = str(input("Enter the float number: "))
    if msg in ["quit", "Quit", "QUIT", "q", "Q", "exit", "EXIT"]:
        clientSock.close()
        break

    print (msg)
    msg = msg.encode()
    clientSock.sendto(msg, (UDP_IP_ADDRESS, UDP_PORT_NO))

    while True:
        data, addr = clientSock.recvfrom(UDP_PORT_NO)
        if data:
            print (data.decode())
            break
