class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []

        def deeper(have):
            if len(have) == n:
                result.append(int(have))
                return

            previous = int(have[-1])
            if previous + k <= 9:
                deeper(have + str(previous + k))
            if previous - k >= 0 and k > 0:
                deeper(have + str(previous - k))

        for i in range(1, 10): # no leading zero
            deeper(str(i))

        return result
