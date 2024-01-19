class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        # empty string is still special
        if not s:
            return s

        parts   = []
        left    = 0
        special = 0 # prefix is special if number of 1s is the same as number of 0s
        for right, c in enumerate(s):
            special += +1 if c == "1" else -1
            if special == 0:
                # yes, it's special
                deeper = self.makeLargestSpecial(s[left + 1 : right])
                parts.append("1" + deeper + "0")
                left   = right + 1

        # lexicographically largest => descending order
        return "".join(sorted(parts, reverse = True))
