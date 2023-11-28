class Solution:
    def balancedStringSplit(self, s: str) -> int:
        result  = 0
        balance = 0
        for c in s:
            if c == "L":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                result += 1

        return result
