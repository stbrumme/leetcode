class Solution:
    def distinctIntegers(self, n: int) -> int:
        # in the end, all numbers [2, n] will be part of the set
        # nevertheless, here's my "simulation" code

        if n == 1:
            return 1

        todo = set([ n ])
        for _ in range(10000):
            next = set()
            for t in todo:
                for i in range(2, n + 1):
                    if i not in todo and t % i == 1:
                        next.add(i)
            todo |= next
            if len(todo) == n - 1:
                break

        return len(todo) # n - 1
