class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        size = len(arr)
        # track what numbers can be found at which positions
        same = defaultdict(list)
        for i, a in enumerate(arr):
            same[a].append(i)

        # assume that each number is present at position 0 and compute sum of intervals
        total = { s: sum(same[s]) for s in same }
        done  = { s: 0            for s in same }

        for i, a in enumerate(arr):
            # same numbers on left and right side
            left  = done[a]
            right = len(same[a]) - left
            # distance to previous occurrence of the same number
            last  = same[a][left - 1] if left > 0 else 0
            gap   = i - last

            # update and emit
            total[a] += left  * gap
            total[a] -= right * gap
            yield total[a]

            done[a] += 1
