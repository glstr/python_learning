#! /bin/python
# encoding=utf-8

import grpc

import rdguard_pb2
import rdguard_pb2_grpc

from pprint import pprint


addr = "10.100.57.125:8765"

 
def hello():
    with grpc.insecure_channel(addr) as channel:
        stub = rdguard_pb2_grpc.GuarderStub(channel)
        res = stub.SayHello(rdguard_pb2.HelloRequest(name="Jim"))
        print res.message


def fury():
    with grpc.insecure_channel(addr) as channel:
        stub = rdguard_pb2_grpc.GuarderStub(channel)
        res = stub.Fury(rdguard_pb2.FuryRequest(
                                    method=1, param='{"room_id":2758101}'))
        if res.error_code != 0:
            print 'error_code:%d, error_msg:%s' % (
                    res.error_code,
                    res.error_msg)
        else:
            pprint(res.result)


if __name__ == '__main__':
    fury()
