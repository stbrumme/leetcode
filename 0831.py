class Solution:
    def maskPII(self, s: str) -> str:
        if s.count("@") > 0:
            # mail
            s = s.lower()
            a, b = s.split("@")
            return a[0] + "*****" + a[-1] + "@" + b

        # phone
        prefix = { 10: "", 11: "+*-", 12: "+**-", 13: "+***-" }
        digits = [ c for c in s if "0" <= c <= "9" ]
        last   = "".join(digits[-4 : ])
        return prefix[len(digits)] + "***-***-" + last
