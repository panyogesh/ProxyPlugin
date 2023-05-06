#!/usr/bin/python3.6

import grpc
from concurrent import futures
import time
import socket
import math

# import the generated classes
import n4_proxy_message_pb2 
import n4_proxy_message_pb2_grpc

# Here we define the UDP IP address as well as the port number that we have
# already defined in the client python script.
PROXY_SERVER_PORT_NO = '50051'

class Calculator:
    def square_root(self, x):
        y = math.sqrt(x)
        return y

# create a class to define the server functions
# derived from calculator_pb2_grpc.CalculatorServicer
class ProxyPluginSerivcer(n4_proxy_message_pb2_grpc.N4ProxyPluginServicer):

    def __init__ (self, name):
        self.name = name 

    # calculator.square_root is exposed here
    # the request and response are of the data types
    # generated as calculator_pb2.Number
    def SquareRoot(self, request, context):
        response = n4_proxy_message_pb2.PFCPAssociationMessage()
        calc=Calculator()
        print (request.value)
        response.value = calc.square_root(request.value)
        return response
     
    def add_to_server (self, server):
        n4_proxy_message_pb2_grpc.add_N4ProxyPluginServicer_to_server (self, server)

# Kind of main.py

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

proxy_srv = ProxyPluginSerivcer("ProxyServer")
proxy_srv.add_to_server(server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
#server.add_insecure_port('[::]:50051')
PORT_CONFIG = "[::]:"+ PROXY_SERVER_PORT_NO

print (PORT_CONFIG)

server.add_insecure_port(PORT_CONFIG)
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
