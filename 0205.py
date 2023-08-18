class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = { }
        t2s = { }
        for i in range(len(s)):
            if s[i] in s2t:
                if s2t[s[i]] != t[i]:
                    return False
            else:
                s2t[s[i]] = t[i]

            t2s[t[i]] = s[i]

        return len(s2t.keys()) == len(t2s.keys())
