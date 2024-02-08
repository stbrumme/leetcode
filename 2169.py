class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        # recursive approach (even though it's probably slower and more complicated than a simple loop)
        if num1 == 0 or num2 == 0:
            return 0

        # make sure num2 >= num1
        if num1 > num2:
            num1, num2 = num2, num1

        return 1 + self.countOperations(num2 - num1, num1)
