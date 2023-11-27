class Solution:
    def knightDialer(self, n: int) -> int:
        # based on https://oeis.org/A327692
        # jump[i] => numbers reachable from i
        jump = [ (4, 6), (6, 8), (7, 9), (4, 8), (3, 9, 0), (), (1, 7, 0), (2, 6), (1, 3), (2, 4) ]
        todo = [1] * 10 # start from each field
        for _ in range(1, n):
            next = [ 0 ] * 10
            for source in range(10):
                for target in jump[source]:
                    next[target] += todo[source]
            todo = next
        return sum(todo) % 1_000_000_007
