class channel:

    def __init__(self, namechannel, nameuser):
        self.channe = namechannel
        self.user = nameuser
        self.queues = [] 
        self.subscribers = []

    def push(self,x):
        self.queues.append(x)

    def pop(self):
        self.channels.pop(0)    


    def pushs(self,x):
        self.subscribers.append(x)

    def pops(self,x):
        self.subscribers.remove(x) 

    def pushq(self,x):
        self.queues.append(x)

    def popq(self,x):
        self.queues.remove(x)  
            
