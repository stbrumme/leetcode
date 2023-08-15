class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if num == "0":
            return "0"
        if k >= len(num):
            return "0"

        again = True
        while k > 0 and again:
            again = False
            for i in range(len(num) - 1):
                if num[i+1] < num[i]:
                    num = num[0:i] + num[i+1:]
                    k -= 1
                    again = True
                    break

        if k > 0:
            num = num[0:-k]
        while len(num) > 1 and num[0] == "0":
            num = num[1:]

        return num
