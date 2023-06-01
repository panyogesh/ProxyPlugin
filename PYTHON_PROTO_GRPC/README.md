# UDP to GRPC conversion

Contains a minimal working example for converting UDP message to GRPC messages

## Quickstart

```shell
git clone https://github.com/panyogesh/ProxyPlugin.git
cd ProxyPlugin/PYTHON_PROTO_GRPC
pip install -r requirements.txt
python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. n4_proxy_message.proto
./udp_client.py (25)--> n4_proxy_plugin.py (25) -> n4_proxy_server.py
                    <-5 (Response sqrt(25))     <- 5 (Response sqrt(25))
```                                             

## File reference
```
udp_client.py      : Sending float value to calculate floating point number
n4_proxy_plugin.py : Reading from UDP socket and sending over to GRPC
n4_proxy_server.py : Actual server which will do Square root calculation 
```
