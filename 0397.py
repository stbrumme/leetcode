class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0

        loops = set()
        dp = set([ n ])
        iterations = 0
        while True:
            iterations += 1

            next = set()
            for x in dp:
                if x in loops:
                    continue

                if x == 2: # x // 2 => 1 or x - 1 => 1
                    return iterations

                loops.add(x)

                if x % 2 == 0:
                    next.add(x // 2)
                else:
                    next.add(x - 1)
                    next.add(x + 1)

            dp = next

        return -1
