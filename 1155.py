class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        todo = defaultdict(int)
        todo[0] = 1
        for m in range(n):
            next = defaultdict(int)
            for i in range(target):
                for j in range(k, 0, -1):
                    if i + j <= target:
                        next[i + j] += todo[i]
            todo = next
        return todo[target] % 1_000_000_007
