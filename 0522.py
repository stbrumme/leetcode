class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        # a whole string can be a subsequence, too
        # let's find the longest string that isn't a subsequence of any other string
        # it will be faster to check longest strings first

        # shortest words first
        strs.sort(key = lambda x : len(x))

        # find duplicates
        skip = set()
        have = set()
        for s in strs:
            if s in have:
                skip.add(s)
            have.add(s)

        def partOf(long, short): # True if short is a subsequence of long and short != long
            if len(long) < len(short) or long == short: # long == short simplifies the any() construct below
                return False

            # greedy matching of short and long
            l = s = 0
            while l < len(long) and s < len(short):
                if long[l] == short[s]:
                    s += 1
                l += 1
            return s == len(short)

        # compare each string against all longer strings
        for short in reversed(strs):
            if short not in skip and not any([ partOf(long, short) for long in strs ]):
                return len(short)

        return -1
