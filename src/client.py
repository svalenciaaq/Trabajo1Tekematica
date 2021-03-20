
import socket



# create an ipv4 (AF_INET) socket object using the tcp protocol (SOCK_STREAM)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
queues=[]
option = 0
# connect the client
# client.connect((target, port))
client.connect(('192.168.1.104', 80))
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
def close_connection():
	client.close()
	print("close connection")

def create_queue():
	
	namequeue = input()
	msg = "queue" + " " + namequeue 
	client.send(str.encode(msg))

def delete_queue():

	namequeue = input()
	msg = "deleteq" + " " + namequeue + " " + name
	client.send(str.encode(msg))

def show_queues():
	client.send(str.encode("showq"))
	client.send(str.encode(name))
	q = client.recv(2048).decode().rstrip("\n")
	l = q.split(" ")
	id= 0
	print(" \n")
	print("QUEUES \n")
	for i in l:
		if i != '':
			queues.append(i)
			print(str(id + 1 )+". " + i )
			id+=1



	

while True:
	print("Choose an option \n")
	print("QUEUE")
	print("1. Create a queue \n")
	print("2. delete a qeueu \n")
	print("3. show queues \n")
	
	option = float(input("Ingrese la opcion \n"))

	if option == 1:
		create_queue()
		client.close()
		break
	
	if option == 2:
		delete_queue()


	if option == 3:
		show_queues()	

	if option == 7:
		close_connection()
		break	


