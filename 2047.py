class Solution:
    def countValidWords(self, sentence: str) -> int:
        valid = 0
        tokens = sentence.split(" ")
        for t in tokens:
            if not t: # multiple spaces => empty tokens
                continue

            # no digits
            if re.search("[0-9]", t):
                continue

            # punctuation only at the end
            if t[-1] in [ "!", ".", "," ]:
                t = t[:-1]
                 # could be empty now
                if not t:
                    valid += 1
                    continue

            # no more punctuation
            if re.search("[\!\.\,]", t):
                continue

            # at most one hyphen
            if t.count("-") > 1:
                continue
            if t[0] == "-" or t[-1] == "-":
                continue

            valid += 1

        return valid
