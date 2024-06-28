class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        size = len(num)
        num  = [ int(n) for n in num ]

        again = True
        replace = False
        for i, n in enumerate(num):
            if change[n] >= n:
                replace = True
            elif replace and not again:
                break

            if replace:
                if num[i] < change[n]:
                    num[i] = change[n]
                    again  = False

        return "".join(str(n) for n in num)
