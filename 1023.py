class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        # convert to regular expression:
        # allow a-z before and after each letter of pattern
        regex = "^[a-z]*"
        for p in pattern:
            regex += p
            regex += "[a-z]*"
        regex += "$"

        # use Python's matching
        result = []
        for q in queries:
            yield re.match(regex, q) != None
