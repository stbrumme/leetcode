class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        # create all substrings
        dots = defaultdict(list)
        for i in range(len(t)):
            for j in range(i + 1, len(t) + 1):
                phrase = t[i : j]
                # replace each single letter by a dot and remember the original phrase/substring
                for k in range(len(phrase)):
                    regex = phrase[:k] + "." + phrase[k + 1:]
                    dots[regex].append(phrase)

        result = 0
        # and repeat the same for s
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                phrase = s[i : j]
                for k in range(len(phrase)):
                    regex = phrase[:k] + "." + phrase[k + 1:]
                    # look up
                    if regex in dots:
                        for d in dots[regex]:
                            # avoid self-matching (the dot must represent a different character)
                            if d != phrase:
                                result += 1

        return result
