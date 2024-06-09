class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        # sum of all rolls, including known and unknown
        need  = (n + len(rolls)) * mean
        # sum of known rolls
        need -= sum(rolls)

        # impossible ?
        if need < n or need > 6 * n:
            return []

        while n > 0:
            dice  = need // n
            need -= dice
            n    -= 1
            yield dice
