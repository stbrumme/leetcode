class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        have = [ 0 ]
        for row in mat:
            next = []

            for value in set(row): # process only unique values
                for h in have:
                    next.append(h + value)
                    if h + value >= target: # next one will be even larger, can't be closer to target
                        break

            have = sorted(set(next))

        result = +inf
        for h in have:
            result = min(result, abs(h - target))
            if h > target:
                break
        return result
