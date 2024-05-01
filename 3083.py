class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        def hash(a, b):
            return (ord(a) - 97) * 26 + ord(b) - 97

        have = [ False ] * (26 * 26)
        for a, b in zip(s, s[1:]):
            have[hash(a, b)] = True
            if a == b or have[hash(b, a)]: # early exit
                return True

        for a, b in zip(s, s[1:]):
            if have[hash(b, a)]:
                return True

        return False
