Implementation and use of the system
This document explains in a step-by-step manner how the system was implemented and how it is used.
To begin with, we started by developing a server and a client that could connect to each other. For that we used the methods provided by socket in Python. 
client
![image.png](/.attachments/image-bf317475-5fb3-45ed-87fe-063b1385bd08.png)
 
server
 ![image.png](/.attachments/image-ff0e1147-e112-4df9-b85f-1322551990df.png)
Then, with a connection already established, we proceeded to generate a client authentication process, asking for username and password and storing this information in a hashtable on the server. In case the user already exists it verifies that the password matches, if it does not exist it will create a new one. 



Client
  ![image.png](/.attachments/image-db399f1b-8f54-4d65-9953-f6aa1c8624b0.png)
Server 
 ![image.png](/.attachments/image-d1e11b92-59dc-45ae-a85a-d06ff4b64031.png)
With these connection and verification steps we proceed to develop all the application logic.
For this, a series of methods were created in both the client and the server. These methods serve as communicators depending on what the client wants to do. 
The Queue, Channel and Message classes had to be developed for the correct functioning of the application. 
Each class and the client and server methods will be explained below.
**Queue**
Class that creates queue type objects with unique names associated to a user and with a list of messages.
**Attributes:** 
- Name: Queue name, this will be unique.
- User: User who created it, this will only be used to be deleted by him.
- Message: List of messages that the queue will store.
**Methods:**
- Push: receive a message and store it in the message list.
- Pop: Pops the message in the first position of the message list.

**Messages**
Class that creates message type objects.
**Attributes:** 
- User: User that sends it.
- Queue: Name of the queue to which it is sent.
- Data: Message information

**Channels**
Class that creates channel type objects which will have a unique name, subscribers, subscriber queues, and a user creator.
**Attributes:** 
- Channe: Channel name
- User: Creator user
- Queues: list of subscriber queues
- Subscribers: list of subscribers
**Methods:** 
- Pushq: saves a queue in the queue list
- Popq: returns a queue from the queue list
- Pushs: Saves a subscriber in the subscribers list
- Pops: Returns a subscriber from the subscribers list

**Using the system**
1.	Eject the client.py file as long as the server is already running, otherwise run the server.
2. We will be asked for user and password, we create one or enter the data of an already created account.
 ![image.png](/.attachments/image-ab4ba558-58df-467a-9ea5-676971a72c2a.png)
3. We will select an option of the 16 available ones. 
 ![image.png](/.attachments/image-eddff610-e47e-4762-9ae3-ee1fe8ff04a9.png)
4.	Create a queue will allow us to create a new queue asking for a name, if the name is already created it will not allow us to create it. 
 ![image.png](/.attachments/image-89847991-3960-444f-95ee-7add058ae3b3.png)
5.	Delete a queue allows us to delete a queue created by entering the name, if the queue does not exist or we are not the creators, it will not allow us to delete it.
 ![image.png](/.attachments/image-99c5dbb7-a957-43d0-b397-ca31c3b590dd.png)
6.	Show my queues will show the queues created by the user, if there are no queues it will show the corresponding message.
 ![image.png](/.attachments/image-f77beeee-2e54-4c2b-ab94-1ab303019937.png)
7.	Show all queues will show all the queues created and by which user it was created.
 ![image.png](/.attachments/image-9d36a1ed-d521-4a87-a4c0-9558039886fa.png)
8.	Send a message to a queue will allow us to send a message to a specific queue, for this it will ask for the queue name. In case it does not exist, it will show the corresponding message.
 ![image.png](/.attachments/image-2733ba39-2404-426a-a4b0-e028a5a165b1.png)
9.	Pull message from a queue allows us to pull a message from a specific queue, for this it will ask for the queue name. In case the queue does not exist or there are no messages it will show the corresponding message, otherwise it will return the stored message.
 ![image.png](/.attachments/image-7e02cf75-234d-4504-b653-8c1265297703.png)
10.	Create a Chanel creates a channel with a unique name, in case it already exists it will not allow to create it.
 ![image.png](/.attachments/image-5320115b-c0ab-4779-9f1c-49c6ea4f617d.png)
11.	Delete a Chanel allows to delete a channel as long as it exists and we are the creators.
 ![image.png](/.attachments/image-43129120-18cf-474d-96b3-5605f3d3f010.png)
12.	Show my chanels, show all channels work like the queue methods.
13.	Show channels I am subscribed show the channels to which you are subscribed, if you are not subscribed nothing will appear.
 ![image.png](/.attachments/image-1e038657-edd2-4ddf-9870-9e16e3b007c3.png)
14.	Send message to a chanel allows you to send a message to a channel as long as you are subscribed and the channel exists. Otherwise it will ask us to subscribe or that the channel does not exist.
 ![image.png](/.attachments/image-4d5b7bdf-e4c2-4ddb-99af-60f4c48b2bdc.png)
15.	Subscribe to Chanel allows us to subscribe to a channel, this means that the messages sent to that channel will be stored in a queue to which we will be able to look at our messages.
 ![image.png](/.attachments/image-3e7e773e-adc1-4dbc-8d4c-8ff868fc338a.png)
16.	Pull a message from a chanel allows us to pull a message from our channel queue as long as we are subscribed at the time the message was sent, otherwise it will show its respective message. 
 ![image.png](/.attachments/image-0bc4783e-d948-4029-86c6-d4505d822363.png)
17.	Close connection closes the session. 
![image.png](/.attachments/image-fcd345c3-25a5-44e5-b879-69d4c05c67c4.png)