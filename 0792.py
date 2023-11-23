class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        def match(sub, subPos, full, fullPos):
            # subsequence complete
            if subPos == len(sub):
                return True
            # match next letter
            next = full.find(sub[subPos], fullPos)
            return match(sub, subPos + 1, full, next + 1) if next != -1 else False

        result = 0
        for w in words:
            # Python Regex works but is too slow
            #regex = ".*".join([ c for c in w ])
            #if re.search(regex, s):
            #    result += 1

            if match(w, 0, s, 0):
                result += 1
        return result
