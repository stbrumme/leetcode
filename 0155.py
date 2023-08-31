class MinStack:

    def __init__(self):
        self.data = []
        self.min  = []

    def push(self, val: int) -> None:
        self.data.append(val)
        lowest = val if not self.min else self.min[-1]
        self.min.append(val if val < lowest else lowest)

    def pop(self) -> None:
        self.data.pop()
        self.min.pop()

    def top(self) -> int:
        return self.data[-1]

    def getMin(self) -> int:
        return self.min[-1]
