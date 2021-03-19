class channel:

    def __init__(self, queue, user):
        self.namequeue = queue
        self.nameuser = user
        self.channe = [] 

    def push(self,x):
        self.channe.append(x)

    def pop(self):
        self.channe.pop(0)    
        

