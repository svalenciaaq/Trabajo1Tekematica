import base64
import socket
import os
from Queue import queue
import threading
import hashlib
import json
from message import message
import time
from channels import channel

# Create Socket (TCP) Connection
ServerSocket = socket.socket(family = socket.AF_INET, type = socket.SOCK_STREAM) 
host = '127.0.0.1'
print(host)
port = 1233
ThreadCount = 0
login = ""


try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection...')
ServerSocket.listen(10)
HashTable = {}
queu= []
chann= []
subscribers = []
qe = ""
queuesubscriber = ""

# Function : For each client 
def threaded_client(connection):
    connection.send(str.encode('Username: ')) # Request Username
    name = connection.recv(2048)
    connection.send(str.encode('Password: ')) # Request Password
    password = connection.recv(2048)
    password = password.decode()
    name = name.decode()
    password=hashlib.sha256(str.encode(password)).hexdigest() # Password hash using SHA256
 # REGISTERATION PHASE   
    
# If new user,  regiter in Hashtable Dictionary  
    if name not in HashTable:
        HashTable[name]=password
        login = "Registeration Successful"
        connection.send(str.encode(login)) 
        print('Registered : ',name)
        print("{:<8} {:<20}".format('USER','PASSWORD'))
        for k, v in HashTable.items():
            label, num = k,v
            print("{:<8} {:<20}".format(label, num))
        print("-------------------------------------------")

        f = open ('holamundo.txt','a')
        mensaje = "\n"+ name +" "+password 
        f.write(mensaje)
        print(mensaje)
        f.close()
        
    else:
# If already existing user, check if the entered password is correct
        if(HashTable[name] == password):
            login = "'Connection Successful"
            connection.send(str.encode(login)) # Response Code for Connected Client 
            print('Connected : ',name)
        else:
            login = "Login Failed"
            connection.send(str.encode(login)) # Response code for login failed
            print('Connection Denied : ',name)

    while (login != "Login Failed"):

        # Commands Queue and Channels
        # Qeueu- Create a queue
        # MessageQ= Senda message to a queue
        
        z = connection.recv(2048)
        dec = base64.b64decode(z).decode()
        print(type(dec))
        cmd = json.loads(dec)
        print(cmd)
        if(cmd["cmd"] == 'queuesubscriber'):
            queuesubscriber = cmd["queue"]
            print("entre")
            break
            

        if(cmd["cmd"] == 'queue'):
            create_queue(cmd["namequeu"],name,connection)
            break

        if(cmd["cmd"] == 'showaq'):
          showall_queue(name,connection)
          break     
        if(cmd["cmd"] == 'showmq'):
          showmy_queue(name,connection)
          break    
          
        if(cmd["cmd"] == 'delete'):
            delete_qeueu(cmd["namequeu"], name, connection)
            break
        if(cmd["cmd"] =='sendq'):
           sendq(name,cmd["namequeue"],cmd["data"], connection)
           break
           
        if(cmd["cmd"] == 'close'):
            break    

        if(cmd["cmd"]  == 'pullq'):
            pullq(cmd["queue"],connection)
            break    
        

        if(cmd["cmd"] == 'channel'):
            create_channel(cmd["channel"], name,connection)
            break

        if(cmd["cmd"] ==  'deletec'):
            delete_channel(cmd["channel"],name,connection)
            break

        if(cmd["cmd"] == 'showmc'):
            show_channel(name,connection)  
            break  

        if(cmd["cmd"] ==  "subscribec"):
            subscribe_channel(cmd["namequeue"],name,connection)
            break

        if(cmd["cmd"] == 'sendc'):
            sendc(name,cmd["namequeue"],cmd["data"],connection)
            break

    connection.close()
    print("The connection to client " + name +" has been closed.")        



def showmy_queue(x, con):
    queuesname = []
    for i in queu:
        if(i.user == x):
         queuesname.append(i.queu)
    j ={
        "data": queuesname
    }    
    ju = json.dumps(j)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded)



def showall_queue(x, con):
    queuesname = []
    info = ""
    for i in queu:
        info = "Queue \"" + i.queu + "\" created by \"" + i.user + "\""
        queuesname.append(info)
    j ={
        "data": queuesname
    }    
    ju = json.dumps(j)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded)               




def delete_qeueu(x,y,con):
    j = ""
    correctUser = False
    queueExist = False
    for i in queu:
        if(i.queu == x):
            queueExist = True
            if(i.user == y):
                correctUser = True
                queu.remove(i)
            break    
    if(correctUser):
        j = "Queue \"" + x + "\" deleted successfully!"
    if(not correctUser and queueExist):
        j = "You can't deleted this queue because you did not created it" 
    if(not correctUser and not queueExist):
        j = "There is no queue named \"" + x + "\". Press 1 to create one"
    je = {
        "data": j
    }   
    ju = json.dumps(je)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded)         




def create_queue(x,y,con):
    q = queue(x, y)
    j = ""
    alreadyCreated = False
    for i in queu:
          if(i.queu == x):
            alreadyCreated = True
            break 
    if(alreadyCreated):
        j = "Queue named \"" + x +"\" is already created"
        print("Queue named \"" + x +"\" is already created") 
    else:
        j = "Queue named \"" + x +"\" created successfully!"
        queu.append(q)
    je = {
        "data": j
    }   
    ju = json.dumps(je)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded)          


def sendq(x,y,z,con):
    j = ""
    msg = message(x,y,z)
    
    j = "There is no Queue named \"" + msg.queue + "\"!"
    for i in queu:
        if i.queu == msg.queue:
            i.push(msg.data)
            print(i.messages)
            j = "Message saved sucessfully!"
            break
        
            
    je = {
        "data": j
    }   
    ju = json.dumps(je)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded) 

def pullq(x,con):
    j=""
    mess = ""
    queueExist = False
    j = "There is no Queue named \"" + x + "\""
    for i in queu:
        if i.queu == x:
            mess = i.pop()
            if(mess == ""):
                j = "No messages found in Queue \"" + x + "\"" 
                print("no messages found!")
            else:
                j =  "Message: " + mess
                print(j)
            break
    je = {
        "data": j
    }   
    ju = json.dumps(je)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded)                


def create_channel(x,y,con):
    if len(chann) == 0:
        c = channel(x,y)
        chann.append(c)
        print(chann)
        j={
            "data": "channel create"
        }
        ju =  json.dumps(j)
        enc = str.encode(ju)
        encoded = base64.b64encode(enc)
        con.send(encoded)     
    else:
        for i in chann:
            if i.channe != x:
                c = channel(x,y)
                j={
                    "data": "Channel create"
                }
                ju =  json.dumps(j)
                enc = str.encode(ju)
                encoded = base64.b64encode(enc)
                con.send(encoded)     
            else:
                j={
                    "data": "the channel you are trying to create already exists"
                }
                ju =  json.dumps(j)
                enc = str.encode(ju)
                encoded = base64.b64encode(enc)
                con.send(encoded)     



def delete_channel(x,y,con):
    if len(chann) != 0:
        for i in chann:
            if(i.user == y):
                if(i.channe == x):
                    chann.remove(i)
                    j={
                    "data": "Delete successfully"
                    }
                    ju =  json.dumps(j)
                    enc = str.encode(ju)
                    encoded = base64.b64encode(enc)
                    con.send(encoded)                      

    else:
        j={
            "data": "There are no channels for deleting"
        }
        ju =  json.dumps(j)
        enc = str.encode(ju)
        encoded = base64.b64encode(enc)
        con.send(encoded)                      


def show_channel(x,con):
    qe = ""
    ro = ""
    if len(chann) != 0:
        for i in chann:
            if(i.user == x):
                qe = i.channe
                ro += qe.rstrip("\n") + " ".rstrip("\n")
    
    else:
        ro = "There are no channels to show"  

    j ={
         "data": ro
    }        
    print(j)  
    ju = json.dumps(j)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)

    con.send(encoded)
    
def showall_channels(x, con):
    channelnames = []
    info = ""
    for i in chann:
        info = "Queue \"" + i.channe + "\" created by \"" + i.user + "\""
        channelnames.append(info)
    j ={
        "data": channelnames
    }    
    ju = json.dumps(j)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded)        


def subscribe_channel(x,y,con):
    if len(chann) != 0:
        for i in chann:
            if i.channe == x:
                i.pushs(y)
                create_queuec(x,y)
                j ={
                "data": "Successfully subscribed"
                }    
                ju = json.dumps(j)
                enc = str.encode(ju)
                encoded = base64.b64encode(enc)
                con.send(encoded)
    else:
        j ={
        "data": "There are no channels to subscribe to"
        }    
        ju = json.dumps(j)
        enc = str.encode(ju)
        encoded = base64.b64encode(enc)
        con.send(encoded)    


def create_queuec(x,y):
    q = queue(x, y)
    subscribers.append(q)
    print(subscribers)



def sendc(x,y,z,con):
    j = ""
    msg = message(x,y,z)
    
    j = "There is no Queue named \"" + msg.queue + "\"!"
    for i in chann:
        if i.channe == msg.queue:
            i.push(msg.data)
            j = "Message saved sucessfully!"
            for n in subscribers:
                if n.queu == i.channe:
                        n.push(msg.data)
                        print(n.messages)
                        print("hasta aqui entre")
            break         
    je = {
        "data": j
    }   
    ju = json.dumps(je)
    enc = str.encode(ju)
    encoded = base64.b64encode(enc)
    con.send(encoded) 


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