from heapq import heappush, heapify, heappop
from copy import deepcopy
class priority_queue:
    '''
    This Handle All dataType correctly , be it int, string, tuple.
    It is min-heap by default. So for max-heap store int as -x.
    For max-heap on String store as (-ord(w[0]),w).
    '''
    def __init__(self,A:list=None):
        self.pq = []
        self.n = 0
        if A is not None:
            self.n += len(A)
            self.pq = deepcopy(A)
            heapify(self.pq)
    def empty(self):
        return self.n==0
    def top(self):
        if self.empty():
            return "*"
        return self.pq[0]
    def pop(self):
        if self.empty():
            return "*"
        self.n -= 1
        return heappop(self.pq)

    def push(self,x):
        self.n += 1
        heappush(self.pq,x)


if __name__ == "__main__":
    pass