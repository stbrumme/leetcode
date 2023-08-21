class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()

        result = ""
        while len(s) > k:
            result = s[-k:] + "-" + result
            s = s[:-k]
        result = s + "-" + result
        return result.rstrip("-")
