class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        todo = [ "a", "b", "c" ]
        for i in range(1, n):
            next = []
            for t in todo:
                if t[-1] != "a":
                    next.append(t + "a")
                if t[-1] != "b":
                    next.append(t + "b")
                if t[-1] != "c":
                    next.append(t + "c")
            todo = next

        if k > len(todo):
            return ""

        todo.sort()
        return todo[k - 1]
