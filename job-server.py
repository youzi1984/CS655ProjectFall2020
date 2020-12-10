# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket
from threading import Thread
import time
 
ADDRESS = ('172.17.2.13', 9007)  # address
 
g_socket_server = None
 
g_conn_pool = []  # connections pool

msgs = []

def init():
    """
    initilize server
    """
    global g_socket_server
    
    g_socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create a socket object
    g_socket_server.bind(ADDRESS) #associate the socket with a specific network interface and port number
    g_socket_server.listen(5)  #enable a server to accept() connections
    print("Sever is on, wait for client and workers...")
    
def accept_worker():
    """
    Accept new connection
    """
    while True:
        worker, _ = g_socket_server.accept()  #block and wait for an incoming connection
        # add into coonections pool
        g_conn_pool.append(worker)
        # build thread for each worker
        thread = Thread(target=message_handle, args=(worker,))
        thread.setDaemon(True)
        thread.start()
    
    

def message_handle(worker):
    """
    messages interaction
    """
    # worker.sendall("connect sever successfully!".encode(encoding='utf8'))
    
    while True:
        bytes = worker.recv(1024)
        msgs.append(bytes.decode(encoding='utf8'))

        print("message from worker:", bytes.decode(encoding='utf8'))

        if len(bytes) == 0: #doesn't matter, not important

            worker.close()
            g_conn_pool.remove(worker)
            print("one worker is down.")
            break



if __name__ == '__main__':
    init()

    client, _ = g_socket_server.accept()  # block and wait for an incoming web
    # client.sendall("connect sever successfully!".encode(encoding='utf8'))
    # add client into connections pool
    g_conn_pool.append(client)

    
    # new tread, accept workers
    thread = Thread(target=accept_worker)
    thread.setDaemon(True)
    thread.start()
    
    #wait for all incoming workers
    while True:
        if len(g_conn_pool) == 11:
            break
    
    for i in range(1, len(g_conn_pool)):
        g_conn_pool[i].sendall("All parts are connected!".encode())
    print("All parts are connected!")
    ans = "None\n"
    flag = True
    while True:
        print(msgs)
        #msgs.clear()
        print("Waiting from web:")
        if not flag:
            while(True):
                time.sleep(10)
                if len(msgs) > 0 and len(msgs[-1]) > 7:
                    request = msgs[-1].decode()
                    break

        # print("request:")
        if (flag):
            request = client.recv(1024).decode()
        print("request"+str(request))
        # print("aaaa")
        request = request.split("\t")
        md5_data = str(request[0])
        print("md5 data:"+ str(md5_data))
        # print(md5_data)
        num_of_worker = int(request[1])
        print("num of worker:"+str(num_of_worker))
        # print(num_of_worker)
        for i in range(num_of_worker):
            msg= md5_data+" "+str(num_of_worker)+" "+str(i)
            g_conn_pool[i+1].sendall(msg)
        
        while True:
            time.sleep(2)
            
            if len(msgs) > 0:
                # print(3)
                print(msgs)
                for j in range(len(msgs)):
                    if len(msgs[j].encode())==5:
                        ans = msgs[j]
                        msgs = []
                        break
                
            if ans != "None\n":
                # print(4)
                print(ans)
                break
            # print(5)
        if not flag:
            g_conn_pool[-1].send(ans.encode())
        if flag:
            client.send(ans.encode())
            flag = False
        ans = "None\n"

