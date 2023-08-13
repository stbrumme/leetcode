class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        sum = 1
        for i in range(2, num):
            if i*i > num:
                break
            if num % i == 0:
                sum += i
                if i*i < num:
                    sum += num // i

        return sum == num
