class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        if len(str1) == 0:
            return ""

        if len(str1) > 1 and gcd(len(str1), len(str2)) == 1:
            return ""

        result = ""
        current = ""
        for c in str1:
            current += c
            pattern = "^(" + current + ")+$"
            if re.search(pattern, str1) and re.search(pattern, str2):
                result = current

        return result
