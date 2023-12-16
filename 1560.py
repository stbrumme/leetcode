class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        # no need to look at laps, only start and finish matter
        a = rounds[0]
        b = rounds[-1]
        if a <= b:
            return range(a, b + 1)
        else:
            return chain(range(1, b + 1), range(a, n + 1))
