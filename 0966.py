class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        # pseudo-regex: replace vowels with dots
        regex = lambda x : re.sub("[aeiou]", ".", x.lower())

        hashed   = set()
        nocase   = {}
        patterns = {}
        for w in wordlist:
            # faster lookup than plain list (needed in next phase)
            hashed.add(w)

            # keep only the first
            key = w.lower()
            if key not in nocase:
                nocase  [key] = w

            key = regex(w)
            if key not in patterns:
                patterns[key] = w

        for q in queries:
            # correct word
            if q in hashed:
                yield q
                continue

            q = q.lower()
            # caps
            if q in nocase:
                yield nocase[q]
                continue

            # vowels
            r = regex(q)
            if r in patterns:
                yield patterns[r]
                continue

            # unknown
            yield ""
