# Demo Application showing usage of Scurid Edge Agent

import edgeagent_pb2
import edgeagent_pb2_grpc
import grpc

addr = 'localhost:4040'  # update the server and port accordingly

channel = grpc.insecure_channel(addr)  # starting a local only channel
stub = edgeagent_pb2_grpc.ScuridEdgeAgentAPIStub(channel)  # grpc client


def createidentitydemo():
    try:
        ireq = edgeagent_pb2.CreateDeviceIdentityReq()
        req = stub.CreateDeviceIdentity(ireq)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        print(req)

def registerIdentity():
    try:
        ireq = edgeagent_pb2.RegisterDeviceIdentityReq()

        
        req = stub.RegisterDeviceIdentity(ireq)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        print(req)


def signwithidentitydemo():
    i = 'did:scurid:0x8c5Fa241EbE29490D3968c97C2860d0c7BA102f4'  # this is generated by createidentitydemo
    p = 'GPS:123;Speed:120'
    try:
        ireq = edgeagent_pb2.SignWithIdentityReq(payload=p, did=i)
        req = stub.SignWithIdentity(ireq)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        print(
            req)  # expect result looking something like this 0xce4b09889eb418a7855d9d4f5e4eda5b2faca5a8fcdb70ed2bbc0ba087f44ec27c2e7ef912fdabadc916b9e65e79665980309eee73e8bb4558d0faf95a3a85b21b


def verifysignaturedemo():
    s = '0xd933ab35e55c5e3540294a1e0672da21c27ecda367713ae52c0154130ce1c2800c25ca3999b3864459059f5ad55910b1a27ce7eb270a2b7a750b162e6b52cfca1c'  # this is generated by signwithidentitydemo
    p = 'GPS:123;Speed:120'  # demo value
    i = 'did:scurid:0x8c5Fa241EbE29490D3968c97C2860d0c7BA102f4'
    try:
        ireq = edgeagent_pb2.VerifySignatureReq(signature=s, payload=p,
                                                did=i)  # input message structure is defined in the proto file
        req = stub.VerifySignature(ireq)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        print(req)  # expect T/F response based on the verification done above


if __name__ == '__main__':
    createidentitydemo()
    signwithidentitydemo()
    verifysignaturedemo()