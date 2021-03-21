import json
import socket
import base64


# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
queues=[]
option = 0
# connect the client
# client.connect((target, port))
client.connect(('192.168.1.104', 1233))
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


print("hola")

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
	namequeue = input()
	j = {
		"cmd": "queue",
		"namequeu": namequeue
	}
	cifrar(j)

def delete_queue():

	namequeue = input()
	j = {
		"cmd": "delete",
		"namequeu": namequeue
	}
	cifrar(j)

def show_queues():
	j = {
		"cmd": "showq"
	}
	ju = json.dumps(j)
	enc = str.encode(ju)
	encoded = base64.b64encode(enc)
	client.send(encoded)
	q = client.recv(2048).decode()
	ju = json.loads(q)
	print(type(ju["data"]))
	print(" \n")
	print("QUEUES \n")
	
def sendq():
	namequeue= input("Ingrese el nombre de la cola que quiere enviar el mensaje")
	data = input("Ingrese el mensaje que quiere enviar")
	j = {
		"cmd": "sendq",
		"user": name,
		"namequeue": namequeue,
		"data": data
	}
	cifrar(j)
	

while True:
	print("Choose an option \n")
	print("QUEUE")
	print("1. Create a queue \n")
	print("2. delete a qeueu \n")
	print("3. show queues \n")
	print("7. Close connection \n")
	
	option = float(input("Ingrese la opcion \n"))

	if option == 1:
		create_queue()
		client.close()
		break
	
	if option == 2:
		delete_queue()


	if option == 3:
		show_queues()	
		client.close()
		break

	if option == 4:
		sendq()
		client.close()
		break

	if option == 7:
		close_connection()
		break	


