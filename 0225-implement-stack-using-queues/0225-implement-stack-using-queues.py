from collections import deque
class MyStack:
    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x) #-->[20,10,30]
        # Move all previous elements behind the new one
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())  # Rotate the queue #--[30,20,10]

    def pop(self):
        return self.q.popleft() if not self.empty() else None

    def top(self):
        return self.q[0] if not self.empty() else None

    def empty(self):
        return len(self.q) == 0
