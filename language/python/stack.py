from collections import deque

class Stack:
    def __init__(self, A=None):
        self.stk = deque()
        self.n = 0
        if A is not None:
            self.n += len(A)
            self.stk.extend(A)
    def pop(self):
        if self.empty():
            return "*"
        self.n-=1
        return self.stk.pop()
            
    def empty(self):
        return self.n == 0

    def top(self):
        if self.empty():
            return "*"
        return self.stk[-1]
    
    def push(self,x):
        self.stk.append(x)
        self.n+=1

if __name__ == "__main__":
    pass