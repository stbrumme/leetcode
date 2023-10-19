class CustomStack:
    def __init__(self, maxSize: int):
        self.data = []
        self.capacity = maxSize

    def push(self, x: int) -> None:
        if len(self.data) < self.capacity:
            self.data.append(x)

    def pop(self) -> int:
        return self.data.pop() if self.data else -1

    def increment(self, k: int, val: int) -> None:
        # brute force
        for i in range(min(len(self.data), k)):
            self.data[i] += val
