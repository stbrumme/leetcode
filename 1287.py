class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]

        have = 0
        prev = -1
        for a in arr:
            if a == prev:
                have += 1
                if have * 4 > len(arr):
                    return a
            else:
                have  = 1
            prev = a
