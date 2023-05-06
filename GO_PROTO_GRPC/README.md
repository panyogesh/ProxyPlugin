# Quick snapsot for go & grpc based client and server

## Reference
* https://towardsdatascience.com/grpc-in-golang-bb40396eb8b1

## Pre-Requisites
* Go Package : go version go1.19.8 linux/amd64
  - go get -u github.com/golang/protobuf/protoc-gen-go
  - go get -u github.com/go-openapi/swag

## Enviornmental Setting
* echo $GOROOT :- /usr/local/go
* export GOPATH=$GOPATH:/home/vagrant/ProxyPlugin/GO_PROTO_GRPC
* echo $GOPATH :- /home/vagrant/go:/home/vagrant/ProxyPlugin/GO_PROTO_GRPC

## Directory Structure

* Proto Files:    /home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/           'protos/ protos/models/'
* Golang Package: /home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/go_package 'protos/  protos/models/'

## Proto Commands 

* Following commands for protos
 
```
protoc  --proto_path=/home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/protos/models  --go_out=plugins=grpc:/home/vagrant/ProxyPlugin/GO_PROTO_GRPCsrc/ /home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/protos/models/*.proto

protoc  --proto_path=/home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/protos/  --go_out=plugins=grpc:/home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/ /home/vagrant/ProxyPlugin/GO_PROTO_GRPC/src/protos/*.proto
```

## Client & Server
* grpcServer.go & grpcClient.go
* go run grpcServer.go
* go run grpcClient.go
