class queue:
    def __init__(self, namequeue,nameuser):
        self.user = nameuser
        self.namequeu = namequeue
        self.messages =[]

    def push(self,x):
        self.messages.append(x)

    def pop(self):
        self.messages.pop(0)    

    def get_username(self):

        return self.user

    def get_queuename(self):

        return self.namequeu
    def get_queue(self):

        return self.messages


