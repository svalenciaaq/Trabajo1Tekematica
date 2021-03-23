class channel:

    def __init__(self, namechannel, nameuser):
        self.channe = namechannel
        self.user = nameuser
        self.channels = [] 
        self.subscribers = []

    def push(self,x):
        self.channels.append(x)

    def pop(self):
        self.channels.pop(0)    


    def pushs(self,x):
        self.channels.append(x)

    def pops(self,x):
        self.channels.remove(x)    
            
