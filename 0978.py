class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        result = 1

        prev = 0 # sign of previous pair
        span = 1 # length of current turbulent subarray
        for a, b in zip(arr, arr[1 :]):
            # kind of half-turbulent: same number as before
            if a == b:
                span = 1
                prev = 0
                continue

            sign = +1 if a < b else -1
            if sign == prev:
                span   = 2
            else:
                prev   = sign
                span  += 1
                result = max(result, span)

        return result
