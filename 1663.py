class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        # build an array where each 1 <= value <= 26 and try to "spend" k on the right-most values
        num = [ 1 ] * n # at least 1
        k  -= n         # 1 * n = n
        for i in range(n - 1, -1, -1):
            add = min(26 - num[i], k) # as much as possible, but no more than 26
            num[i] += add
            k      -= add

        result = ""
        for i in num:
            result += chr(i - 1 + ord("a"))
        return result
