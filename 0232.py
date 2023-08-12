class MyQueue:
    stack = []

    def reverse(self, s):
        result = []
        while (len(s) > 0):
            result.append(s.pop())
        return result


    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        other = self.reverse(self.stack)
        result = other.pop()
        self.stack = self.reverse(other)
        return result

    def peek(self) -> int:
        other = self.reverse(self.stack)
        result = other.pop()
        self.stack.append(result)
        while (len(other) > 0):
            self.stack.append(other.pop())
        return result

    def empty(self) -> bool:
        return len(self.stack) == 0
