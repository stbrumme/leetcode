class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        result   = 0
        triangle = 0 # triangle numbers
        for i in range(1, 10**5):
            if n <= triangle:
                break

            if (n - triangle) % i == 0:
                result += 1

            triangle += i

        return result