class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        one   = sum(1 << i for i in range(n))
        two   = sum(1 << i for i in range(1, n, 2))
        three = sum(1 << i for i in range(0, n, 2))
        four  = sum(1 << i for i in range(0, n, 3))

        todo = set([ one ])
        for i in range(presses):
            next = set()
            for t in todo:
                next.add(t ^ one)
                next.add(t ^ two)
                next.add(t ^ three)
                next.add(t ^ four)
            todo = next

        return len(todo)
