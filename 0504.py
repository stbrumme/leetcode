class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return "0"

        isNeg = False
        if num < 0:
            isNeg = True
            num = -num

        result = ""
        while num != 0:
            result = result + str(num % 7)
            num //= 7

        result = result[::-1]

        if isNeg:
            return "-" + result
        else:
            return       result
