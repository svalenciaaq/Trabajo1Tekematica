from Queue import queue
import socket



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


print("hola")
def close_connection():
	client.close()
	print("close connection")

def create_queue():
	
	namequeue = input()
	client.send(str.encode("queue"))
	client.send(str.encode(namequeue + "\n"))
	client.send(str.encode(name))


def show_queues():
	client.send(str.encode("showq"))
	
	client.send(str.encode(name))
	q = client.recv(2048).decode()
	queues.append(q)
	print("\n")
	print("Queus \n")
	id= 1
	for i in queues:
		print(str(id)+". " + i)
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

	if option == 3:
		show_queues()	

	if option == 7:
		close_connection()
		break	


