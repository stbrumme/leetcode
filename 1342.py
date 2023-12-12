class Solution:
    def numberOfSteps(self, num: int) -> int:
        result = 0
        while num > 0:
            result += num & 1
            num   >>= 1
            if num > 0:
                result += 1
        return result
