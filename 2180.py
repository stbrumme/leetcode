class Solution:
    def countEven(self, num: int) -> int:
        result = 0

        even = 1 # 1 = True, 0 = False
        for i in range(1, num + 1):
            if i % 10 > 0:
                even ^= 1
            else:
                digitsum = 0
                x = i
                while x > 0:
                    digitsum += x % 10
                    x       //= 10

                even = (digitsum & 1) ^ 1

            result += even

        return result
