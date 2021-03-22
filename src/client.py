import json
import socket
import base64


# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
queues=[]
option = 0
# connect the client
# client.connect((target, port))
client.connect(('127.0.0.1', 1233))
response = client.recv(2048)
# Input UserName
name = input(response.decode())	
client.send(str.encode(name))
response = client.recv(2048)
# Input Password
password = input(response.decode())	
client.send(str.encode(password))
''' Response : Status of Connection :
	1 : Registeration successful 
	2 : Connection Successful
	3 : Login Failed
'''
# Receive response 
response = client.recv(2048)
response = response.decode()

print(response)

def cifrar(x):
	ju = json.dumps(x)
	enc = str.encode(ju)
	encoded = base64.b64encode(enc)
	client.send(encoded)

def close_connection():
	
	j = {
		"cmd": "close"
	}
	cifrar(j)
	
	print("close connection")
	client.close()

def create_queue():	
	
	namequeue = input("Queue Name: ")
	j = {
		"cmd": "queue",
		"namequeu": namequeue
	}
	cifrar(j)
	q = client.recv(2048)
	dec = base64.b64decode(q).decode()
	cmd = json.loads(dec)
	if(cmd["data"] == ""):
		print("No messages found in queue \"" + namequeue + "\"!")
	else:
		print(cmd["data"])
	
	

def delete_queue():

	namequeue = input("Queue Name to Delete: ")
	j = {
		"cmd": "delete",
		"namequeu": namequeue
	}
	cifrar(j)
	q = client.recv(2048)
	dec = base64.b64decode(q).decode()
	cmd = json.loads(dec)
	print(cmd["data"])

def showmy_queues():
	j = {
		"cmd": "showmq"
	}
	cifrar(j)
	q = client.recv(2048)
	dec = base64.b64decode(q).decode()
	cmd = json.loads(dec)
	print("My Queues")
	for i in cmd["data"]:

		print(i)
		
def showall_queues():
	j = {
		"cmd": "showaq"
	}
	cifrar(j)
	q = client.recv(2048)
	dec = base64.b64decode(q).decode()
	cmd = json.loads(dec)
	print("All Queues")
	
	for i in cmd["data"]:

		print(i)
		
	
def sendq():
	namequeue= input("Queue Name: ")
	data = input("Your Message: ")
	j = {
		"cmd": "sendq",
		"user": name,
		"namequeue": namequeue,
		"data": data
	}
	cifrar(j)
	q = client.recv(2048)
	dec = base64.b64decode(q).decode()
	cmd = json.loads(dec)
	print(cmd["data"])
	
def pullq():
	que=  input("Queue name you want your message from: ")
	j = {
		"cmd": "pullq",
		"queue": que

	}
	cifrar(j)
	q = client.recv(2048)
	dec = base64.b64decode(q).decode()
	cmd = json.loads(dec)
	print(cmd["data"])

def queue_subscribe():
	qu = input("Enter the queue you want to subscribe to")
	j ={
		"cmd":"queuesubscriber",
		"queue": qu
	}
	ju = json.dumps(j)
	enc = ju.encode()
	encoded= base64.b64encode(enc)
	client.send(encoded)


while True:
	print("\n")
	print("Choose An Option ")
	print("QUEUE OPTION")
	print("1. Create a queue ")
	print("2. Delete a qeueu ")
	print("3. Show my queues ")
	print("4. Send message to a queue")
	print("5. Pull message from a queue")
	print("7. Close connection \n")
	print("8. Show all queues")
	
	option = float(input("Input your option \n"))

	if option == 1:
		create_queue()
		client.close()
		break	
	
	if option == 2:
		delete_queue()
		client.close()
		break
		

	if option == 3:
		showmy_queues()	
		client.close()
		break	

		
	if option == 4:
		sendq()
		client.close()
		break	

	if(option == 5):
		pullq()
		client.close()
		break	

	if(option == 6):
		queue_subscribe()
		client.close()
		break	
	if option == 7:
		close_connection()
		break	
	if option == 8:
		showall_queues()
		client.close
		break


