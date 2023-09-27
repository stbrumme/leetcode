class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result = ""
        for p in permutations(arr):
            hour   = p[0] * 10 + p[1]
            minute = p[2] * 10 + p[3]
            if hour < 24 and minute < 60:
                current = str(hour).zfill(2) + ":" + str(minute).zfill(2)
                result  = max(result, current)

        return result
