class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        if sum(machines) % len(machines) > 0:
            return -1

        final  = sum(machines) // len(machines)
        total  = 0
        result = 0
        for m in machines:
            diff    = m - final
            total  += diff
            result  = max(result, abs(total), diff)

        return result