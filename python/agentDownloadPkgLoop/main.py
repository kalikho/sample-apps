# Demo Application showing Download functionality by edge agent

import edgeagent_pb2
import edgeagent_pb2_grpc
import grpc
import calendar
import time
import os
<<<<<<< HEAD
<<<<<<< HEAD
import string
import random
=======
>>>>>>> 6c99b40 (added files)
=======
import string
import random
>>>>>>> 54f8808 (removed user inputs)


addr = 'localhost:4040'  # update the server and port accordingly, addr corresponds to an agent
channel = grpc.insecure_channel(addr)  # starting a local only channel
stub = edgeagent_pb2_grpc.ScuridEdgeAgentAPIStub(channel)  # grpc client

def createidentitydemo():
    try:
        ireq = edgeagent_pb2.CreateDeviceIdentityReq()
        req = stub.CreateDeviceIdentity(ireq)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        return req.did

def registerIdentity(identity_name):
    param1 = createidentitydemo()
    param2 = calendar.timegm(time.gmtime())
    param3 = identity_name
    try:
        ireq = edgeagent_pb2.RegisterDeviceIdentityReq(did=param1,unixTime=param2,deviceName=param3)

        
        req = stub.RegisterDeviceIdentity(ireq)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        print(" ")
        print("Identity generated successfully")
        print(" ")
        print("Identity DID : ", param1)
        print("Identity Name : ",param3)
        print("Timestamp : ", param2)
        print(" ")
<<<<<<< HEAD
<<<<<<< HEAD
        print("Switch to the App, approve identity, and set artifacts")
    return param1
=======
        print("Switch to the App and approve identity")
>>>>>>> 6c99b40 (added files)
=======
        print("Switch to the App, approve identity, and set artifacts")
    return param1
>>>>>>> 54f8808 (removed user inputs)


def downloadpkg(identity,storagePath):
    try:
        param1 = identity #approved identity
        param2 = storagePath #full path where the file needs to be stored
        counter = 0
        if not os.path.exists(param2):
            os.makedirs(param2)

<<<<<<< HEAD
<<<<<<< HEAD
        while(1):
            counter = counter + 1
            ireq = edgeagent_pb2.DownloadFilesReq(identity=param1,path=param2)
            try:
                req = stub.DownloadFiles(ireq)
                print("==== downloading ====")
                print("Download attempt - ",counter)
            except Exception as e:
                print("error: ",e.details)
<<<<<<< HEAD
=======
        print("==== downloading ====")
=======
>>>>>>> 54f8808 (removed user inputs)
        while(1):
            counter = counter + 1
            ireq = edgeagent_pb2.DownloadFilesReq(identity=param1,path=param2)
<<<<<<< HEAD
            req = stub.DownloadFiles(ireq)
>>>>>>> 6c99b40 (added files)
=======
            try:
                req = stub.DownloadFiles(ireq)
                print("==== downloading ====")
                print("Download attempt - ",counter)
            except Exception as e:
                print("error: ",e.details)
>>>>>>> 54f8808 (removed user inputs)
            time.sleep(3)
=======
            time.sleep(1)
>>>>>>> 68ff609 (updated sleep to 1 sec)
    except grpc.RpcError as e:
        print(f'failed setting: {e.details}')
    else:
        print(" ")
        print("Package downloaded at location: ",param2)

if __name__ == '__main__':
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 54f8808 (removed user inputs)
        N = 7
        identityname = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=N))
        identity = registerIdentity(identityname)
        storagePath = "downloads/"+identity
        downloadpkg(identity,storagePath)
<<<<<<< HEAD
=======
    while(1):
        print(" ")
        print("1. Generate Identity")
        print("2. Download Package")
        print("3. Exit")
        print(" ")
        choice = input('Select your operation ')
        print(" ")
        
        if choice == "1":
            name = input("Identity Name ")
            registerIdentity(name)
        if choice == "2":
            identity = input("Identity DID : ")
            storagePath = input("Storage Path : ")
            downloadpkg(identity,storagePath)
        if choice == "3":
            exit()
>>>>>>> 6c99b40 (added files)
=======
>>>>>>> 54f8808 (removed user inputs)
