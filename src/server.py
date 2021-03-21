import socket
import os
from Queue import queue
import threading
import hashlib
import json

import time


# Create Socket (TCP) Connection
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
host = '0.0.0.0'
print(host)
port = 1233

ThreadCount = 0


try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen(10)
HashTable = {}
queu= []
qe = ""

# Function : For each client 
def threaded_client(connection):
    connection.send(str.encode('ENTER USERNAME : ')) # Request Username
    name = connection.recv(2048)
    connection.send(str.encode('ENTER PASSWORD : ')) # Request Password
    password = connection.recv(2048)
    password = password.decode()
    name = name.decode()
    password=hashlib.sha256(str.encode(password)).hexdigest() # Password hash using SHA256
 # REGISTERATION PHASE   
    
# If new user,  regiter in Hashtable Dictionary  
    if name not in HashTable:
        HashTable[name]=password
        connection.send(str.encode('Registeration Successful')) 
        print('Registered : ',name)
        print("{:<8} {:<20}".format('USER','PASSWORD'))
        for k, v in HashTable.items():
            label, num = k,v
            print("{:<8} {:<20}".format(label, num))
        print("-------------------------------------------")
        
    else:
# If already existing user, check if the entered password is correct
        if(HashTable[name] == password):
            connection.send(str.encode('Connection Successful')) # Response Code for Connected Client 
            print('Connected : ',name)
        else:
            connection.send(str.encode('Login Failed')) # Response code for login failed
            print('Connection denied : ',name)

    while True:

        # Commands Queue and Channels
        # Qeueu- Create a queue
        # MessageQ= Senda message to a queue
        z = connection.recv(2048).decode()
        
        cmd = json.loads(z)

        print(cmd)

        if(cmd["cmd"] == 'queue'):
            create_queue(cmd["namequeu"],name)
            break
            
        if(cmd == 'messageq'):
            namequeu = connection.recv(2048).decode()


        if(cmd["cmd"] == 'showq'):
          show_queue(name,connection)
          break       

        if(cmd[0] == 'deleteq'):
            delete_qeueu(cmd[1], name)
    connection.close()
    print("the connection to client " + name +" has been closed.")        

def show_queue(x, con):
    qe = ""
    ro = ""
    for i in queu:
        if(i.user == x):
            qe = i.queu
            ro += qe.rstrip("\n") + " ".rstrip("\n")
    j ={
        "data": ro
    }    
    ju = json.dumps(j)     
    con.send(str.encode(jus))             

def delete_qeueu(x,y):
    for i in queu:
        if(i.user == y):
            if(i.queu == x):
                queu.remove(i)


def create_queue(x,y):
      q = queue(x, y)
      queu.append(q)

while True:
    Client, address = ServerSocket.accept()
    client_handler = threading.Thread(
        target=threaded_client,
        args=(Client,)  
    )
    client_handler.start()
    ThreadCount += 1
    print('Connection Request: ' + str(ThreadCount))
ServerSocket.close()