class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def deeper(a, b, s):
            if not s:
                return False

            need = a + b
            if need == int(s):
                if need > 0 and s[0] != "0":
                    return True
                if need == 0 and s == "0":
                    return True

            for length in range(1, len(s)):
                # no leading zeros
                if s[0] == "0" and length > 1:
                    return False

                have = int(s[:length])
                if have == need:
                    return deeper(b, have, s[length:])
                if have > need:
                    return False
            return False

        for i in range(1, len(num)):
            for j in range(i+1, len(num)):
                a = int(num[:i])
                b = int(num[i:j])

                # no leading zeros
                if num[0] == "0" and i > 1:
                    break
                if num[i] == "0" and j - i > 1:
                    break

                if deeper(a, b, num[j:]):
                    return True

        return False
