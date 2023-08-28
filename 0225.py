class MyStack:
    def __init__(self):
        self.queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        # one almost full rotation
        x = self.queue.pop(0)
        for _ in range(len(self.queue)):
            self.queue.append(x)
            x = self.queue.pop(0)
        return x

    def top(self) -> int:
        result = self.pop()
        self.push(result)
        return result

    def empty(self) -> bool:
        return len(self.queue) == 0
