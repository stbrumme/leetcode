class Solution:
    def addDigits(self, num: int) -> int:
        if (num < 10):
            return num

        sum = 0
        while num > 0:
            sum = sum + num % 10
            num = num // 10

        return self.addDigits(sum)
