class queue:

    def __init__(self, namequeue,nameuser):
        self.queu = namequeue
        self.user = nameuser
        self.messages = []

    def push(self,x):
        self.messages.append(x)

    def pop(self):
        self.messages.pop()    
        

 

