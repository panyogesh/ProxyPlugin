#!/usr/bin/python3.6

import grpc
from concurrent import futures
import time
import socket

# import the generated classes
import n4_proxy_message_pb2 
import n4_proxy_message_pb2_grpc 


PROXY_SERVER_PORT_NO = '50051'

class MessageRelay:
    UDP_IP_ADDRESS = "127.0.0.1"
    UDP_PORT_NO = 5009 

    def __init__(self, stub):
        self.stub = stub

    def udp_server_pfcp_listner(self):
        serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        serverSock.bind((self.UDP_IP_ADDRESS, self.UDP_PORT_NO))

        while True:
            data, addr = serverSock.recvfrom(self.UDP_PORT_NO)
            print (data.decode())
            output=self.grpc_client_pfcp_message_processor(data.decode())
            print(output)
            msg = str(output).encode()
            serverSock.sendto (msg, addr)

    def grpc_client_pfcp_message_processor (self, reference):
        number = float(reference)
        assoc_msg=n4_proxy_message_pb2.PFCPAssociationMessage(value=number) 
        response=self.stub.SquareRoot(assoc_msg)
        return response.value

server_port_config="localhost:" + PROXY_SERVER_PORT_NO
print (server_port_config)
channel = grpc.insecure_channel(server_port_config)
stub = n4_proxy_message_pb2_grpc.N4ProxyPluginStub(channel)
msg_relay = MessageRelay(stub)
msg_relay.udp_server_pfcp_listner()

