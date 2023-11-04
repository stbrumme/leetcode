class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        # bigger is always better ...
        if k >= len(arr):
            return max(arr)

        if k == 1:
            return max(arr[:2])

        high = arr[0]
        wins = -1 # workaround for comparison of first element against itself
        for a in arr:
            if high >= a:
                wins += 1
                if wins == k:
                    return high
            else:
                wins = 1
                high = a

        # high == max(arr)
        return high
