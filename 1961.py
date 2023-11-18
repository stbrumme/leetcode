class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        have = ""
        for w in words:
            have += w
            if len(have) == len(s):
                return have == s
            if len(have) >  len(s):
                break
        return False
