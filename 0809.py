class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        # let's try some regulaaar expreeession maaatching
        stretchy = 0
        for w in words:
            w += "!" # stop marker

            regex = ""
            prev  = ""
            count = 0
            for c in w:
                if c != prev:
                    if count > 0:
                        regex += "(" + prev * count + "|" + prev * max(3, count) + "+)"
                        count  = 0

                count += 1
                prev   = c

            if re.search("^" + regex + "$", s):
                stretchy += 1
        return stretchy
