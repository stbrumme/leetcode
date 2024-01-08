class Solution:
    def minMaxDifference(self, num: int) -> int:
        low = high = num
        s = str(num)
        for i in range(10):
            x = str(i)
            low  = min(low,  int(s.replace(x, "0")))
            high = max(high, int(s.replace(x, "9")))

        return high - low
