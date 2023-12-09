class Solution:
    def largestOddNumber(self, num: str) -> str:
        while num and num[-1] not in "13579":
            num = num[:-1]
        return num
