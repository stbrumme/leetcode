class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        result = arr[0]

        # current subarray with zero or one deletion
        zero = arr[0]
        one  = arr[0]
        for a in arr[1 :]:
            # append or delete
            one   = max(one + a, zero)
            # append
            zero += a

            # restart
            one  = max(one,  a)
            zero = max(zero, a)

            result = max(result, zero, one)

        return result
