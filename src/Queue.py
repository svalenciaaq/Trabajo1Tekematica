class queue:

    def __init__(self, namequeue,nameuser):
        self.queu = namequeue
        self.user = nameuser
        self.messages = []

    def push(self,x):
        self.messages.append(x)

    def pop(self):
     mess = ""
     if not self.messages:
         return mess
     else:
      mess = self.messages.pop(0)
      return mess
