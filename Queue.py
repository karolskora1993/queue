class Queue:
    def __init__(self, size=99):
        self.size=size
        self.items=[]
    def set_size(self, size):
        self.size=size
    def get_size(self):
        return self.size
    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    def isFull(self):
        if len(self.items)==self.size:
            return  True
        else:
            return False
    def enqueue(self, value):
        if len(self.items)==self.size:
            return False
        else:
            self.items.append(value)
            return True
    def dequeue(self):
        if len(self.items)==0:
            return None
        else:
            x=self.items.pop(0)
            return x
    def print(self):
        for i in self.items:
            print(i)


