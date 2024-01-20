class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        result = 0

        size = len(arr)
        # for each number find the distance of the next smaller number
        # do this for the left and the right side
        left  = [ None ] * size
        right = [ None ] * size

        # scan from left to right
        low = [] # position of last minimum
        for i in range(size):
            while low and arr[low[-1]] > arr[i]:
                low.pop()

            if low:
                left[i] = i - low[-1]
            else:
                left[i] = i + 1 # extend to the beginning

            low.append(i)

        # scan from right to left
        low = []
        for i in reversed(range(size)):
            while low and arr[low[-1]] >= arr[i]: # careful: count duplicate numbers only once, therefore >= instead of >
                low.pop()

            if low:
                right[i] = low[-1] - i
            else:
                right[i] = size - i # extend to the end

            low.append(i)

        # all combinations
        for a, l, r in zip(arr, left, right):
            result += a * l * r

        return result % 1_000_000_007
