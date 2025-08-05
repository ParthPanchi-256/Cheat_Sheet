from collections import deque

class Queue:
    def __init__(self,A=None):
        self.q = deque()
        self.n = 0
        if A is not None:
            self.n += len(A)
            self.q.extend(A)
    def empty(self):
        return self.n==0
    def front(self):
        if self.empty():
            return "*"
        return self.q[0]
    def pop(self):
        if self.empty():
            return "*"
        self.n-=1
        return self.q.popleft()
    def push(self,x):
        self.q.append(x)

if __name__=="__main__":
    pass