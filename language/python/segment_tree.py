import sys
from math import gcd
from typing import Callable

class SegmentTree:
    def __init__(self, A, op: Callable, identity):
        self.n = len(A)
        self.op = op              # Operation like sum, max, min, gcd
        self.identity = identity  # Neutral value for that operation
        self.tree = [identity] * (2 * self.n)

        for i in range(self.n):
            self.tree[self.n + i] = A[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, index, value):
        i = index + self.n
        self.tree[i] = value
        while i > 1:
            i //= 2
            self.tree[i] = self.op(self.tree[2 * i], self.tree[2 * i + 1])

    def query(self, l, r):  # [l, r)
        res = self.identity
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                res = self.op(res, self.tree[l])
                l += 1
            if r % 2:
                r -= 1
                res = self.op(res, self.tree[r])
            l //= 2
            r //= 2
        return res

if __name__=="__main__":
    A = [5, 3, 7, 2]  # binary: [101, 011, 111, 010]

    # Sum Segment Tree
    st_sum = SegmentTree(A, op=lambda a, b: a + b, identity=0)
    print("Sum [1, 4):", st_sum.query(1, 4))  # 3 + 5 + 7 = 15

    # Max Segment Tree
    st_max = SegmentTree(A, op=max, identity=-sys.maxsize)
    print("Max [1, 4):", st_max.query(1, 4))  # max of 3, 5, 7 = 7

    # Min Segment Tree
    st_min = SegmentTree(A, op=min, identity=sys.maxsize)
    print("Min [1, 4):", st_min.query(1, 4))  # min of 3, 5, 7 = 3

    # GCD Segment Tree
    st_gcd = SegmentTree(A, op=gcd, identity=0)
    print("GCD [1, 4):", st_gcd.query(1, 4))  # gcd(3, 5, 7) = 1

    # Bitwise AND
    st_and = SegmentTree(A, op=lambda a, b: a & b, identity=~0)
    print("AND [0, 4):", st_and.query(0, 4))  # 5 & 3 & 7 & 2 = 0

    # Bitwise OR
    st_or = SegmentTree(A, op=lambda a, b: a | b, identity=0)
    print("OR [0, 4):", st_or.query(0, 4))    # 5 | 3 | 7 | 2 = 7

    # Bitwise XOR
    st_xor = SegmentTree(A, op=lambda a, b: a ^ b, identity=0)
    print("XOR [0, 4):", st_xor.query(0, 4))  # 5 ^ 3 ^ 7 ^ 2 = 3
