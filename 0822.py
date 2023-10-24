class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        result = invalid = float("inf")

        ignore = set()
        for a, b in zip(fronts, backs):
            # if a == b then it's impossible to keep that number on one side only
            if a == b:
                ignore.add(a)

        for a, b in zip(fronts, backs):
            x = min(a, b)
            y = max(a, b)
            if x not in ignore:
                result = min(result, x)
            if y not in ignore:
                result = min(result, y)

        return 0 if result == invalid else result
