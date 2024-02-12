class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        if abs(endPos - startPos) > k:
            return 0 # too far (actually this check isn't needed, but speeds up the code)

        todo = defaultdict(int)
        todo[startPos] = 1

        for _ in range(k):
            next = defaultdict(int)
            for t in todo:
                next[t - 1] += todo[t]
                next[t + 1] += todo[t]
            todo = next

        return todo[endPos] % 1_000_000_007
