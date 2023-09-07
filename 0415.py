class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        if l1 < l2:
            num1 = ("0" * (l2 - l1)) + num1
            l1 = l2
        if l2 < l1:
            num2 = ("0" * (l1 - l2)) + num2

        carry = 0
        result = ""
        for i in range(l1 - 1, -1, -1):
            a = ord(num1[i]) - ord('0')
            b = ord(num2[i]) - ord('0')

            c = a + b + carry
            if c >= 10:
                carry = 1
                c -= 10
            else:
                carry = 0

            result += str(c)

        if carry == 1:
            result += "1"

        # building in reverse is faster than prepending single digits a thousand times
        return result[::-1]
