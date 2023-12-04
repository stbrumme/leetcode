class Solution:
    def largestGoodInteger(self, num: str) -> str:
        for i in range(9, -1, -1):
            iii = str(i) * 3
            if num.count(iii) > 0:
                return iii
        return ""
