from collections import deque

if __name__ == "__main__":
    dq = deque()
    dq.append(1)
    dq.appendleft(2)
    print(dq[0], dq[-1])
    print(dq.pop())
    print(dq.popleft())