# Implementation and use of the system**

This document explains in a step-by-step manner how the system was implemented and how it is used.
To begin with, we started by developing a server and a client that could connect to each other. For that we used the methods provided by socket in Python. 

## client
![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/c1.png)
 
 
## server
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/s1.png)
 
Then, with a connection already established, we proceeded to generate a client authentication process, asking for username and password and storing this information in a hashtable on the server. In case the user already exists it verifies that the password matches, if it does not exist it will create a new one. 


## Client

  ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/c2.png)
  
  
## Server 
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/s2.png)
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/s3.png)


With these connection and verification steps we proceed to develop all the application logic.
For this, a series of methods were created in both the client and the server. These methods serve as communicators depending on what the client wants to do. 
The Queue, Channel and Message classes had to be developed for the correct functioning of the application. 
Each class and the client and server methods will be explained below.
## **Queue**
Class that creates queue type objects with unique names associated to a user and with a list of messages.
### **Attributes:** 
- Name: Queue name, this will be unique.
- User: User who created it, this will only be used to be deleted by him.
- Message: List of messages that the queue will store.
### **Methods:**
- Push: receive a message and store it in the message list.
- Pop: Pops the message in the first position of the message list.

## **Messages**
Class that creates message type objects.
### **Attributes:** 
- User: User that sends it.
- Queue: Name of the queue to which it is sent.
- Data: Message information

## **Channels**
Class that creates channel type objects which will have a unique name, subscribers, subscriber queues, and a user creator.
### **Attributes:** 
- Channe: Channel name
- User: Creator user
- Queues: list of subscriber queues
- Subscribers: list of subscribers
### **Methods:** 
- Pushq: saves a queue in the queue list
- Popq: returns a queue from the queue list
- Pushs: Saves a subscriber in the subscribers list
- Pops: Returns a subscriber from the subscribers list

## **Using the system**
* 1.	Eject the client.py file as long as the server is already running, otherwise run the server.
* 2. We will be asked for user and password, we create one or enter the data of an already created account.

 ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/1.png)

* 3. We will select an option of the 16 available ones. 



* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/2.png)
* 4.	Create a queue will allow us to create a new queue asking for a name, if the name is already created it will not allow us to create it. 
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/3.png)
* 5.	Delete a queue allows us to delete a queue created by entering the name, if the queue does not exist or we are not the creators, it will not allow us to delete it.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/4.png)
* 6.	Show my queues will show the queues created by the user, if there are no queues it will show the corresponding message.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/5.png)
* 7.	Show all queues will show all the queues created and by which user it was created.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/6.png)
* 8.	Send a message to a queue will allow us to send a message to a specific queue, for this it will ask for the queue name. In case it does not exist, it will show the corresponding message.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/7.png)
* 9.	Pull message from a queue allows us to pull a message from a specific queue, for this it will ask for the queue name. In case the queue does not exist or there are no messages it will show the corresponding message, otherwise it will return the stored message.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/8.png) 
* 10.	Create a Chanel creates a channel with a unique name, in case it already exists it will not allow to create it.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/9.png)
* 11.	Delete a Chanel allows to delete a channel as long as it exists and we are the creators.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/10.png)
* 12.	Show my chanels, show all channels work like the queue methods.
* 13.	Show channels I am subscribed show the channels to which you are subscribed, if you are not subscribed nothing will appear.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/11.png)
* 14.	Send message to a chanel allows you to send a message to a channel as long as you are subscribed and the channel exists. Otherwise it will ask us to subscribe or that the channel does not exist.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/12.png)
* 15.	Subscribe to Chanel allows us to subscribe to a channel, this means that the messages sent to that channel will be stored in a queue to which we will be able to look at our messages.
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/13.png)
* 16.	Pull a message from a chanel allows us to pull a message from our channel queue as long as we are subscribed at the time the message was sent, otherwise it will show its respective message. 
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/15.png)
* 17.	Close connection closes the session. 
* ![alt text](https://raw.githubusercontent.com/svalenciaaq/Trabajo1Telematica/master/resources/16.png)
